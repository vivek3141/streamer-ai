import argparse
import os
import run

parser = argparse.ArgumentParser(description='Run the program')
parser.add_argument('--gen', metavar='generations', type=int, help='Number of Generations to run for', nargs='?',
                    default=1)
parser.add_argument('--file', metavar='file_name', type=str, help='File name to continue training or to run the winner',
                    nargs='?', default="checkpoints/neat-checkpoint-2492")
parser.add_argument('--config', metavar='config', type=str, help='Configuration File', default='neat.config', nargs='?')

args = parser.parse_args()

run.main(args.gen, args.config, args.file)
os.system("python3 say.py")
