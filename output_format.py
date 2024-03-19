""""
Purpose: Implements OutputFormat functions
Created on Wed Jul 25
Author: Annie_nev
"""
from abc import abstractmethod, ABC


class Output(ABC):
    """
    Allows different output formats
    """
    @abstractmethod
    def read(self):
        pass
