""""
Purpose: Implements OutputFormat functions
Created on Wed Jul 25
Author: Annie_nev
"""


class OutputFormat:
    """
    Allows different output formats
    """
    def __init__(self, data):
        self.data = data

    def console_output(self):
        """
        Prints data to console
        """
        print(self.data)
