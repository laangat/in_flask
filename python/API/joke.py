#!/usr/bin/env python3
import requests

url = "https://v2.jokeapi.dev/joke/Programming?blaclistFlags=nsfw,explicit"
resp = requests.get(url)
print(resp.content.decode())
