from typing import List, AnyStr
from termcolor import colored


def print_desk(desk: List[List[AnyStr]]) -> None:
    for ind, row in enumerate(desk):
        # print(ind + 1, '|', *row)
        print(ind + 1, '|', end=' ')
        for element in row:
            if element == 'R':
                print(colored('R', 'red'), end=' ')
            elif element == 'Y':
                print(colored('Y', 'yellow'), end=' ')
            else:
                print(element, end=' ')
        print()
    print(' ' * 3, '_' * (len(desk[0]) * 2 - 1))
    print(' ' * 3, *range(1, len(desk[0]) + 1))


def add_char(desk: List[List[AnyStr]], char: str, column_ind: int, filled_columns: List[bool]):
    i = len(desk) - 1
    while desk[i][column_ind] != 'E':
        i -= 1
        if i == -1:
            raise IndexError
    desk[i][column_ind] = char
    if i == 0:
        filled_columns[column_ind] = True
    return i
