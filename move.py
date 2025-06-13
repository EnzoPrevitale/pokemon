import requests
from settings import *


class Move:
    def __init__(self, name, endpoint):
        self.name = name
        self.data = requests.get(endpoint).json()
        self.power = self.data["power"]
        self.pp = self.data["pp"]
        self.accuracy = self.data["accuracy"]
        self.type = f"{self.data['type']['name']}"
        self.type = f"{type_colors[self.type]}{self.data['type']['name']}\033[0m"
