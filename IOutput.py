"""
Purpose: Abstract output class.
Created on Wed Jul 25
Author: Annie_nev
"""
from abc import abstractmethod, ABC


class Output(ABC):
    """
    Abstract output class.
    """
    @abstractmethod
    def write(self, data: str):
        """
        Prints the output.
        :param data: The data we want to print.
        """
        pass
