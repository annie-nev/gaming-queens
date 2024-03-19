"""
Purpose: Create a class that ask for string and return it.
Auther: Roza Hadid
Date: 17.3.2024
"""
from Iinput import InputClass


class ConsoleInput(InputClass):
    """
    Class that heir from InputClass.
    Function that return a string that takes from console input.
    """

    def read(self) -> str:
        """
        Function that gets a variable of string type
        :return: The console_input.
        """
        console_input = input()
        return console_input
