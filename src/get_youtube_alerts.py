import json
import socketio

socket_token = json.load(open("../configs/socket_token.json"))['socket_token']
URL = f"https://sockets.streamlabs.com?token={socket_token}"
sio = socketio.Client()
alerts = []


@sio.on('connect')
def connect():
    print('Connected')


@sio.on('event')
def event(data):
    t = data['type']
    response = ""

    if t == 'donation':
        response = f'Thanks for the {data["message"][0]["amount"]} dollars {data["message"][0]["name"]}! ' \
            f'{data["message"][0]["name"]} says {data["message"][0]["message"][0:50]}'

    if t == 'follow':
        response = f'Thanks for subscribing {data["message"][0]["name"]}!'

    if t == 'subscription':
        response = f'Thanks for being a member {data["message"][0]["name"]}! Welcome to the team!'

    if t == 'superchat':
        response = f'Thanks for the {data["message"][0]["displayString"].replace("$", "").split(".")[0]} dollars ' \
            f'{data["message"][0]["name"]}! {data["message"][0]["name"]} says {data["message"][0]["comment"][0:50]}'

    print(response)


sio.connect(URL)
