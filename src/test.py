import neat
import pickle
import gym, ppaquette_gym_super_mario
import visualize
import gzip


ACTIONS = [
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
]
CONFIG = 'config'
env = gym.make('ppaquette/meta-SuperMarioBros-Tiles-v0')
state = env.reset()
total_score = 0

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     "../neat.config")
genome = pickle.load(open("finisher.pkl", 'rb'))
net = neat.nn.FeedForwardNetwork.create(genome, config)
info = {'distance': 0}
try:
    while total_score < 32000:
        state = state.flatten()
        output = net.activate(state)
        ind = output.index(max(output))
        obs, reward, is_finished, info = env.step(ACTIONS[ind])
        state = obs
        total_score = info["total_reward"]
except KeyboardInterrupt:
    env.close()
    exit()

