"""
Purpose: Create a class that input from a file.
Auther: Roza Hadid
Date: 18.3.2024
"""
from Iinput import InputClass


class FileInput(InputClass):
    """
    Contains a function that receive a file path and return his content.
    """

    def __init__(self, file_path: str):
        """
        Initialization method.
        :param file_path: Path of a file.
        """
        self.file_path = file_path

    def read(self) -> str:
        """
        Open the file and read it.
        :return: What the file contains.
        """
        with open(self.file_path, "r") as my_file:
            return my_file.read()
