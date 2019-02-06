import random
from constants import *


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


def say(info, level):
    distance = info['distance']
    level_name = LEVELS[level]
    max_distance = DISTANCES[level_name]

    low = [
        f"That run wasn't the best run, with an underwhelming score of {distance}.",
        f"Hopefully, we can do better next time. ",
        f"A score of {distance} is not the best. ",
        f"That genome got a bad score of {distance}. ",
        f"That one underperformed with a score of {distance}. ",
        f"Well, hopefully the other genomes can beat {distance}. ",
        f"{distance} isn't the best score we can achieve. ",
        f"Maybe we can beat {distance} next time. ",
    ]

    high = [
        f"Oh wow, that run had a decent score of {distance}. ",
        f"That run had a great score of {distance}. ",
        f"Hopefully, we can keep up this score of {distance}. ",
        f"That run was pretty good, with a score of {distance}. ",
        f"Wow, we are killing it with a score of {distance}. ",
        f"So far we are doing pretty good with that score of {distance}. ",
        f"That one was great with a score of {distance}. ",
        f"Maybe we can keep a score of {distance} up. ",
        f"That was a decent run with a score of {distance}. ",
        f"That run had a score of {distance}. "
    ]

    extreme = [
        f"Oh wow! This run is fantastic, we are doing great by going with a score of {distance}. ",
        f"Wow we just completed {level_name} with a distance of {distance}. ",
        f"{level_name} just flew by! Let's finish the other ones. ",
        f"This is the run, I'm telling you! {level_name} is just too easy. ",
    ]

    if distance <= 0.3 * max_distance:
        if random.randint(1, 2) == 1:
            return low[random.randint(0, len(low) - 1)]

    if max_distance > distance >= 0.7 * max_distance:
        return high[random.randint(0, len(high) - 1)]

    if distance >= max_distance:
        return extreme[random.randint(0, len(extreme) - 1)]

    return ""
