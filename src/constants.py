conf = {i.split(":")[0].strip(): i.split(":")[1].strip() for i in open("config").readlines()}
socket_token = conf['socket_token']

URL = f"https://sockets.streamlabs.com?token={socket_token}"

alerts = []
ACTIONS = [
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1],
]
