from os import system
from supplementary_functions import print_desk, add_char
from checking_functions import check_victory
from termcolor import colored


def main():
    width = 7
    height = 6
    correct_digits = list(map(str, range(1, width + 1)))
    while True:
        desk = [['E'] * width for _ in range(height)]
        filled_columns = [False] * width
        current_turn = 'R'
        print(colored('Connect 4 by @volyomaS', 'green'))
        print(colored('Print 1 to start new game', 'yellow'))
        print(colored('Print 2 to exit', 'yellow'))
        command = input()
        if command == '1':
            while True:
                # Clear console output
                system('cls')

                # Print current turn and desk
                print(colored(f'Current turn: {current_turn} player', 'yellow'))
                print_desk(desk)

                # Ask user to enter column index
                print(colored('Choose column to append (or "exit" to quit): ', 'yellow'), end='')
                column_ind = input()
                if column_ind == 'exit':
                    system('cls')
                    break
                # Check index correctness
                while column_ind not in correct_digits or 0 >= int(column_ind) or int(column_ind) > width or \
                        filled_columns[int(column_ind) - 1]:
                    system('cls')
                    print(colored(f'Current turn: {current_turn} player', 'yellow'))
                    print_desk(desk)
                    print(colored('Wrong column index. Enter new column ind: ', 'yellow'), end='')
                    column_ind = input()

                # Add char to chosen column
                column_ind = int(column_ind) - 1
                row_ind = add_char(desk, current_turn, column_ind, filled_columns)

                # Check victory
                response = check_victory(desk, row_ind, column_ind)
                if response[0]:
                    system('cls')
                    print_desk(desk)
                    print(colored(f'Game end! The winner is {current_turn} {response[2]}', 'red'))
                    break
                # Change turn
                current_turn = 'R' if current_turn == 'Y' else 'Y'
        elif command == '2':
            break
        else:
            system('cls')
            print(colored('Wrong command', 'red'))
    system('cls')
    print(colored('Thanks for playing!', 'green'))


if __name__ == '__main__':
    main()
