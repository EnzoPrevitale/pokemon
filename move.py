import requests
from settings import *


class Move:
    def __init__(self, name, endpoint):
        self.name = name
        self.data = requests.get(endpoint).json()
        self.power = self.data["power"]
        self.pp = self.data["pp"]
        self.accuracy = self.data["accuracy"]
        self.type = f"{type_colors[self.data['type']['name']]}{self.data['type']['name'].title()}\033[0m"
        self.description = f"{self.data['effect_entries'][0]['effect'].replace('\n', '')}" if len(self.data['effect_entries']) > 0 else ""
