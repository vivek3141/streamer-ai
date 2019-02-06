import argparse
import os

parser = argparse.ArgumentParser(description='Run the program')
parser.add_argument('--gen', metavar='generations', type=int, help='Number of Generations to run for', nargs='?',
                    default=1000)
parser.add_argument('--file', metavar='file_name', type=str, help='File name to continue training or to run the winner',
                    nargs='?', default="neat-checkpoint-2547")
parser.add_argument('--config', metavar='config', type=str, help='NEAT Configuration File', default='neat.config', nargs='?')

args = parser.parse_args()

if not os.path.isfile("config"):
    raise Exception("Config file not found!")

os.system(f"python3 src/say.py & python3 src/run.py --gen {args.gen} --file {args.file} --config {args.config}")
