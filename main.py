import argparse
import os

parser = argparse.ArgumentParser(description='Run the program')
parser.add_argument('--gen', metavar='generations', type=int, help='Number of Generations to run for', nargs='?')
parser.add_argument('--file', metavar='file_name', type=str, help='File name to continue training or to run the winner',
                    nargs='?', default="checkpoints/neat-checkpoint-2492")
parser.add_argument('--config', metavar='config', type=str, help='Configuration File', default='neat.config', nargs='?')

args = parser.parse_args()

os.system(f"python3 say.py && python3 run.py --gen {args.gen} --file {args.file} --config {args.config}")


