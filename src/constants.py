conf = {i.split(":")[0].strip(): i.split(":")[1].strip() for i in open("../config").readlines()}
socket_token = conf['socket_token']

URL = f"https://sockets.streamlabs.com?token={socket_token}"

alerts = []
ACTIONS = [
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
]

LEVELS = [f"{x}-{y}" for x in range(1, 9) for y in range(1, 5)]
DISTANCE = [3266, 3266, 2514, 2430, 3298, 3266, 3682, 2430, 3298, 3442, 2498, 2430, 3698, 3266, 2434, 2942, 3282, 3298,
            2514, 2429, 3106, 3554, 2754, 2429, 2962, 3266, 3682, 3453, 6114, 3554, 3554, 4989]

DISTANCES = {LEVELS[i]: DISTANCE[i] - 20 for i in range(len(LEVELS))}
