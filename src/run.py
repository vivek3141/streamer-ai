import json
import socketio
import neat
import gym
import ppaquette_gym_super_mario
import pickle
import visualize as visualize
import random
import argparse

from constants import *
from get_sentences import *

gym.logger.set_level(40)

sio = socketio.Client()


def get_actions(a):
    return ACTIONS[a.index(max(a))]


def fitness_func(genomes, config):
    try:
        idx, genomes = zip(*genomes)

        for genome in genomes:
            level = 0
            env = gym.make(f'ppaquette/SuperMarioBros-{LEVELS[level]}-Tiles-v0')

            state = env.reset()
            net = neat.nn.FeedForwardNetwork.create(genome, config)

            done = False
            i = 0
            old = 40
            fitness = 0

            while True:
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

                fitness += info['distance']

                if info['distance'] >= DISTANCES[level]:
                    if level == len(LEVELS):
                        break
                    level += 1
                    env.close()
                    env = gym.make(f'ppaquette/SuperMarioBros-{LEVELS[level]}-Tiles-v0')
                    env.reset()
                    state, reward, done, info = env.step([0 for i in range(6)])

                else:
                    break

            genome.fitness = fitness
            env.close()

            with open("say.txt", "a+") as f:
                to_write = say(info)

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
        response = donation(data)

    if t == 'follow':
        response = follow(data)

    if t == 'subscription':
        response = subscription(data)

    if t == 'superchat':
        response = superchat(data)

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
