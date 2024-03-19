"""
Purpose: Create an abstract class.
Auther: Roza Hadid
Date: 17.3.2024
"""
from abc import ABC, abstractmethod


class InputClass(ABC):
    """
    Abstract class, Contains abstract function.
    """
    @abstractmethod
    def read(self) -> str:
        """
        Abstract method that read a string.
        """
        pass
