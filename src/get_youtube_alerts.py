import json
import socketio

socket_token = json.load(open("configs/socket_token.json"))['socket_token']
URL = f"https://sockets.streamlabs.com?token={socket_token}"
sio = socketio.Client()
alerts = []


@sio.on('connect')
def connect():
    print('Connected')


@sio.on('event')
def event(data):
    alerts.append(data)


sio.connect(URL)
try:
    while True:
        if alerts != []:
            print(alerts[0])
            del alerts[0]
except KeyboardInterrupt:
    pass
