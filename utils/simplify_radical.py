#!usr/bin/env python
import math
import sys


def simplify_radical(radical):
    '''Returns the most simplified form of the given radical number.

    Args:
        radical (int): an integer representing a radical number.

    Returns:
        str: A string showing the given radical and its simplification (if any).
    '''
    square_root = math.sqrt(radical)
    if square_root.is_integer():
        return '√{} = {}'.format(radical, int(square_root))
    possible_multiple = int(square_root)
    while possible_multiple > 1:
        if (radical / possible_multiple).is_integer():
            possible_whole_number = math.sqrt(radical / possible_multiple)
            if possible_whole_number.is_integer():
                new_radical = possible_multiple
                whole_number = int(possible_whole_number)
                return '√{} = {}√{}'.format(
                    radical, whole_number, new_radical
                )
        possible_multiple -= 1
    return '√{} = √{}'.format(radical, radical)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('A radical number must be provided')
    if len(sys.argv) == 2:
        radical = int(sys.argv[1])
        print(simplify_radical(radical))
