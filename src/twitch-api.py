import urllib.request
import json

config = {i.split(":")[0].strip(): i.split(":")[1].strip() for i in open("config").readlines()}

URL = "https://api.twitch.tv/kraken/channels/" + config['Channel'] + "/follows"
SUB = "https://api.twitch.tv/kraken/channels/" + config['Channel'] + "/subscriptions"

REQUEST = urllib.request.Request(URL)
REQUEST.add_header("Client-ID", config['Client-ID'])

SUBR = urllib.request.Request(SUB)
SUBR.add_header("Client-ID", config['Client-ID'])


def get_last_follower():
    resp = urllib.request.urlopen(REQUEST)
    data = resp.read().decode('utf-8')
    j = json.loads(data)
    return j['follows'][0]['user']['display_name']


def get_subscribers():
    resp = urllib.request.urlopen(SUBR)
    data = resp.read().decode('utf-8')
    j = json.loads(data)
    return j


print(get_subscribers())
"""
lastFollower = get_last_follower()
while True:
    follower = get_last_follower()
    if follower != lastFollower:
        print(f"{follower} has just followed!")
        lastFollower = follower"""
