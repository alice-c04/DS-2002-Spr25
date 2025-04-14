import os
import json
import requests
GHUSER = os.getenv('alice-c04')

url = 'https://api.github.com/users/{alice-c04}/events'.format(GHUSER)
r = json.loads(requests.get(url).text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)

