import neat
import pickle
import gym, ppaquette_gym_super_mario
import visualize
import gzip
from constants import *


def get_actions(a):
    return ACTIONS[a.index(max(a))]


ACTIONS = [
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
]
total_score = 0

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     "../neat.config")
genome = pickle.load(open("finisher.pkl", 'rb'))
net = neat.nn.FeedForwardNetwork.create(genome, config)
info = {'distance': 0}
try:
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
        if info['distance'] >= DISTANCES[LEVELS[level]]:
            if level == len(LEVELS):
                break
            level += 1
            env.close()
            env = gym.make(f'ppaquette/SuperMarioBros-{LEVELS[level]}-Tiles-v0')
            env.reset()
            state, reward, done, info = env.step([0 for i in range(6)])
        else:
            break
except KeyboardInterrupt:
    env.close()
    exit()
finally:
    env.close()
    exit()
