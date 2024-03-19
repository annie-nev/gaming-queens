"""
    Purpose: Console output class.
    Author: Elian
    Date: 19/03/2024
"""
from IOutput import Output


class ConsoleOutput(Output):
    """Console output"""
    def write(self, data: str):
        """
        Manages the console output.
        :param data: The data we want to print.
        """
        print(data)
