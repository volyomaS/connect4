from os import system
from supplementary_functions import print_desk, add_char
from checking_functions import check_victory


def main():
    width = 7
    height = 6
    correct_digits = list(map(str, range(1, width + 1)))
    while True:
        desk = [['E'] * width for _ in range(height)]
        filled_columns = [False] * width
        current_turn = 'R'
        print('Connect 4 by @volyomaS')
        print('Print 1 to start new game')
        print('Print 2 to exit')
        command = input()
        if command == '1':
            while True:
                # Clear console output
                system('cls')

                # Print current turn and desk
                print(f'Current turn: {current_turn} player')
                print_desk(desk)

                # Ask user to enter column index
                print('Choose column to append (or "exit" to quit): ', end='')
                column_ind = input()
                if column_ind == 'exit':
                    system('cls')
                    break
                # Check index correctness
                while column_ind not in correct_digits or 0 >= int(column_ind) or int(column_ind) > width or \
                        filled_columns[int(column_ind) - 1]:
                    system('cls')
                    print(f'Current turn: {current_turn} player')
                    print_desk(desk)
                    print('Wrong column index. Enter new column ind: ', end='')
                    column_ind = input()

                # Add char to chosen column
                column_ind = int(column_ind) - 1
                row_ind = add_char(desk, current_turn, column_ind, filled_columns)

                # Check victory
                response = check_victory(desk, row_ind, column_ind)
                if response[0]:
                    system('cls')
                    print_desk(desk)
                    print(f'Game end! The winner is {current_turn} {response[2]}')
                    break
                # Change turn
                current_turn = 'R' if current_turn == 'Y' else 'Y'
        elif command == '2':
            break
        else:
            system('cls')
            print('Wrong command')
    system('cls')
    print('Thanks for playing!')


if __name__ == '__main__':
    main()
