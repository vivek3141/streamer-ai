import urllib.request
import json

config = {i.split(":")[0].strip(): i.split(":")[1].strip() for i in open("config").readlines()}
URL = "https://api.twitch.tv/kraken/channels/" + config['Channel'] + "/follows"
REQUEST = urllib.request.Request(URL)
REQUEST.add_header("Client-ID", config['Client-ID'])


def get_last_follower():
    resp = urllib.request.urlopen(REQUEST)
    data = resp.read().decode('utf-8')
    j = json.loads(data)
    return j['follows'][0]['user']['display_name']


lastFollower = get_last_follower()

while True:
    follower = get_last_follower()
    if follower != lastFollower:
        print(f"{follower} has just followed!")
        lastFollower = follower
