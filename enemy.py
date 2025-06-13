from pokemon import Pokemon


class Enemy(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level)