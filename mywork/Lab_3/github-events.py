#!/usr/bin/python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')

url = f'https://api.github.com/users/alice-c04/events'
print(f"Fetching events from : {url}")

response = requests.get(url)
r = json.loads(requests.get(url).text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)
