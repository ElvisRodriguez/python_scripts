'''
Module for useful constants and functions.
'''

# Constants

LOWER_ALPHABET = ''.join([chr(i) for i in range(97, 123)])
UPPER_ALPHABET = ''.join([char.upper() for char in LOWER_ALPHABET])

# Functions

def print_iterable(iterable, sep=' '):
    print(*iterable, sep=sep)

