import json
import socketio
import neat
import gym
import ppaquette_gym_super_mario
import pickle
import src.visualize as visualize
import random
import argparse

gym.logger.set_level(40)

conf = {i.split(":")[0].strip(): i.split(":")[1].strip() for i in open("config").readlines()}
socket_token = conf['socket_token']

URL = f"https://sockets.streamlabs.com?token={socket_token}"
alerts = []
ACTIONS = [
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
]

sio = socketio.Client()


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
                state = state.flatten()
                output = net.activate(state)
                output = get_actions(output)

                state, reward, done, info = env.step(output)

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
                    index = max(5, len(alerts))
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


def main(generations, config, checkpoint):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config)

    p = neat.Checkpointer.restore_checkpoint(checkpoint)

    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.Checkpointer(5))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    print("loaded checkpoint...")
    winner = p.run(fitness_func, generations)

    pickle.dump(winner, open('winner.pkl', 'wb'))

    visualize.draw_net(config, winner, True)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the program')
    parser.add_argument('--gen', metavar='generations', type=int, help='Number of Generations to run for', nargs='?',
                        default=1)
    parser.add_argument('--file', metavar='file_name', type=str,
                        help='File name to continue training or to run the winner',
                        nargs='?', default="checkpoints/neat-checkpoint-2492")
    parser.add_argument('--config', metavar='config', type=str, help='Configuration File', default='neat.config',
                        nargs='?')

    args = parser.parse_args()
    main(args.gen, args.config, args.file)
