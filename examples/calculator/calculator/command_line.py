"""
try calculator module using the command line
"""
from .parser import parser

def main():
    """
    compute input line
    """
    print(parser("2.56+5*9/1+9*7"))
