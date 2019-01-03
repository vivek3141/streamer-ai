import json
import socketio

socket_token = json.load(open("socket_token.json"))['socket_token']
URL = f"https://sockets.streamlabs.com?token={socket_token}"
sio = socketio.Client()


@sio.on('connect')
def connect():
    print('Connected')


@sio.on('event')
def event(data):
    print('I received a message!')
    print(data)


sio.connect(URL)
try:
    while True:
        pass
except KeyboardInterrupt:
    pass