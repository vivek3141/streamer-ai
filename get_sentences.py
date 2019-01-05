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
    to_write = [f"Hey that was a decent run with a score of {info['distance']}. ",
                f"That run had a score of {info['distance']}. "][
        random.randint(0, 1)] if info['distance'] > 1000 else ""
    return to_write
