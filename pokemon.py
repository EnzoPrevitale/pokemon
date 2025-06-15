import random
from move import Move
from settings import *


class Pokemon:
    def __init__(self, name, level, data):
        self.name = name
        self.level = level
        self.data = data
        self.moves = []
        self.types = []
        for i in self.data["types"]:
            self.types.append(i['type']['name'])

    def set_moves(self):
        while len(self.moves) < 4:
            move_data = random.choice(self.data["moves"])
            if move_data["version_group_details"][0]["level_learned_at"] <= self.level:
                name = move_data['move']['name'].title()
                endpoint = move_data['move']['url']
                move = Move(name, endpoint)
                self.moves.append(move)

    def __str__(self):
        return f"{type_colors[self.types[0]]}{self.name}\033[0m | Level: {self.level} | Types: {f"{type_colors[self.types[0]]}{self.types[0].title()}" if len(self.types) == 1 else f'{type_colors[self.types[0]]}{self.types[0].title()}\033[0m, {type_colors[self.types[1]]}{self.types[1].title()}'}\033[0m"