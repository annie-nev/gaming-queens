"""
    Purpose: Create an abstract class.
    Author: Maysan Halaby
    Date: 17/03/2024
"""
from abc import ABC, abstractmethod


class Game(ABC):
    """
    Abstract class that represent a game.
    """
    @abstractmethod
    def start_game(self):
        """
        Starts the game.
        """
        pass

    @abstractmethod
    def get_player_move(self):
        """
        Gets the player move by input.
        """
        pass

    @abstractmethod
    def check_win(self):
        """
        Checks if the player has won the game.
        """
        pass

    @abstractmethod
    def end_game(self):
        """
        Ends the game.
        """
        pass
