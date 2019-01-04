import json
import socketio
import neat
import gym, ppaquette_gym_super_mario
import pickle
import gzip
import src.visualize as visualize

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
    env = gym.make('ppaquette/meta-SuperMarioBros-Tiles-v0')
    try:
        for genome in genomes:
            state = env.reset()
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            done = False
            i = 0
            old = 40
            while not done:
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
    except KeyboardInterrupt:
        env.close()
        exit()


@sio.on('connect')
def connect():
    print('Connected')


@sio.on('event')
def event(data):
    alerts.append(data)


sio.connect(URL)


def main(generations):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         "neat.config")
    p = neat.Checkpointer.restore_checkpoint("checkpoints/neat-checkpoint-2492")
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
