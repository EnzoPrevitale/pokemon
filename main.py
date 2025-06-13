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

        player = Player(player_pokemon, 36, data_player)
        player.set_moves()
        for i in player.moves:
            print(f"{i.name} | Power: {i.power} | PP: {i.pp} | Accuracy: {i.accuracy} | Type: {i.type}")


main = Main()
