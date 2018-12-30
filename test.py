import requests
import socketio

socket_token = open("socket_token").read()
access_token = open("access_token").read()

params = {
    "token": socket_token,
    "transports": "websocket",
}
request = requests.request("GET", f"https://sockets.streamlabs.com", params=params)
print(request)

sio = socketio.Client()


@sio.on('connect')
def on_connect():
    print('connection established')


@sio.on('my message')
def on_message(data):
    print('message received with ', data)
    sio.emit('my response', {
        "token": socket_token,
        "transports": "websocket",
    })


@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')


sio.connect("http://sockets.streamlabs.com")
sio.wait()
