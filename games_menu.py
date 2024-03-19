from typing import Dict
from game_class import Game


class GamesMenu:
    def __init__(self, games_dict: Dict[str, Game], input, output):
        self.games_dict = games_dict
        self.input = input
        self.output = output

    def print_menu(self):
        self.output.write(self.games_dict.keys())


