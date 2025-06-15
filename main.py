from pokemon import Pokemon
from player import Player
from enemy import Enemy
import requests


class Main:
    def __init__(self):
        player_pokemon = input("Digite o nome do seu Pokémon: ").title()
        url_player = f"https://pokeapi.co/api/v2/pokemon/{player_pokemon.lower()}/"
        response_player = requests.get(url_player)
        data_player = response_player.json()

        player = Player(player_pokemon, 100, data_player)
        player.set_moves()
        print(player)
        for i in player.moves:
            print(f"\033[97m{i.name} | Power: {i.power} | PP: {i.pp} | Accuracy: {i.accuracy} | Type: {i.type}\n    {i.description}\033[0m")


main = Main()
