import requests
import random
from move import Move


class Pokemon:
    def __init__(self, name, level, data):
        self.name = name
        self.level = level
        self.data = data
        self.moves = []
        self.types = []
        for i in self.data["types"]:
            self.types.append(i["type"]["name"])

    def set_moves(self):
        while True:
            for i in range(4):
                move_data = random.choice(self.data["moves"])["move"]
                name = move_data['name']
                endpoint = move_data['url']
                move = Move(name, endpoint)
                self.moves.append(move)
                move
            break
