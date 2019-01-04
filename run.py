import json
import socketio
import neat
import gym, ppaquette_gym_super_mario
import pickle
import src.visualize as visualize
import random

gym.logger.set_level(40)

socket_token = json.load(open("configs/socket_token.json"))['socket_token']
URL = f"https://sockets.streamlabs.com?token={socket_token}"
sio = socketio.Client()
alerts = []
ACTIONS = [
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
]


def get_actions(a):
    return ACTIONS[a.index(max(a))]


def fitness_func(genomes, config):
    try:
        idx, genomes = zip(*genomes)
        for genome in genomes:
            env = gym.make('ppaquette/meta-SuperMarioBros-Tiles-v0')
            state = env.reset()
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            done = False
            i = 0
            old = 40
            while not done:
                if not (state is None):
                    state = state.flatten()
                output = net.activate(state)
                output = get_actions(output)
                s, reward, done, info = env.step(output)
                state = s
                i += 1
                if i % 50 == 0:
                    if old == info['distance']:
                        break
                    else:
                        old = info['distance']
            genome.fitness = -1 if info['distance'] <= 40 else info['distance']
            env.close()
            with open("say.txt", "a+") as f:
                to_write = [f"Hey that was a decent run with a score of {genome.fitness}. ",
                            f"That run had a score of {genome.fitness}. "][
                    random.randint(0, 1)] if genome.fitness > 1000 else ""
                if alerts != []:
                    index = max(10, len(alerts))
                    f.write(". ".join(alerts[0:index]))
                    del alerts[0:index]
                f.write(to_write)
    except KeyboardInterrupt:
        env.close()
        exit()


@sio.on('connect')
def connect():
    print('Connected')


@sio.on('event')
def event(data):
    t = data['type']
    response = ""
    if t == 'donation':
        response = f'Thanks for the {data["message"][0]["amount"]} dollars {data["message"][0]["name"]}! ' \
            f'{data["message"][0]["name"]} says {data["message"][0]["message"][0:50]}'
    if t == 'follow':
        response = f'Thanks for subscribing {data["message"][0]["name"]}!'
    if t == 'subscription':
        response = f'Thanks for being a member {data["message"][0]["name"]}! Welcome to the team!'
    if t == 'superchat':
        response = f'Thanks for the {data["message"][0]["displayString"].replace("$", "").split(".")[0]} dollars ' \
            f'{data["message"][0]["name"]}! {data["message"][0]["name"]} says {data["message"][0]["comment"][0:50]}'
    alerts.append(response)


sio.connect(URL)


def main(generations):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         "neat.config")
    p = neat.Checkpointer.restore_checkpoint("checkpoints/gen_2284")
    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.Checkpointer(5))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    print("loaded checkpoint...")
    winner = p.run(fitness_func, generations)
    win = p.best_genome
    pickle.dump(winner, open('winner.pkl', 'wb'))
    pickle.dump(win, open('real_winner.pkl', 'wb'))

    visualize.draw_net(config, winner, True)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)


if __name__ == "__main__":
    main(1)
