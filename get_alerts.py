import requests

socket_token = open("socket_token").read()
access_token = open("access_token").read()

params = {
    "token": socket_token,
}
request = requests.request("POST", f"https://sockets.streamlabs.com", params=params)
print(request.text)
