import json
import requests

access = json.load(open("access_token.json"))
print(access)
r = requests.request("GET", 'https://streamlabs.com/api/v1.0/socket/token', params={"access_token":access['access_token']})
print(r.text)
