import json
import random


def donation(data):
    response = f'Thanks for the {data["message"][0]["amount"]} dollars {data["message"][0]["name"]}! ' \
        f'{data["message"][0]["name"]} says {data["message"][0]["message"][0:50]}'
    return response


def subscription(data):
    response = f'Thanks for being a member {data["message"][0]["name"]}! Welcome to the team!'
    return response


def follow(data):
    response = f'Thanks for subscribing {data["message"][0]["name"]}!'
    return response


def superchat(data):
    response = f'Thanks for the {data["message"][0]["displayString"].replace("$", "").split(".")[0]} dollars ' \
        f'{data["message"][0]["name"]}! {data["message"][0]["name"]} says {data["message"][0]["comment"][0:50]}'
    return response


def say(info):
    distance = info['distance']
    low = [
        f"That run was'n t the best run, with an underwhelming score of {distance}.",
        f"Hopefully, we can do better next time.",
        f"A score of {distance} is not the best.",
        f"That genome got a bad score of {distance}.",
        f"That one underperformed with a score of {distance}.",
        f"Well, hopefully the other genomes can beat {distance}.",
        f"{distance} is'nt the best score we can achieve.",
        f""
    ]
    to_write = [f"Hey that was a decent run with a score of {distance}. ",
                f"That run had a score of {distance}. "][
        random.randint(0, 1)] if distance > 1000 else ""
    return to_write
