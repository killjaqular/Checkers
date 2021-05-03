'''
checkers.py

simple checkers game.
'''
#REQUIRED LIBRARIES
###################################################################################################
import numpy

from sys import stdout
from os import system, name

#OBJECTS/CLASSES
###################################################################################################

class game_state:
    end_game = False

    player_turn = 'PLAYER_ONE'

class gameboard:
    VERTICAL_BORDER   = '|'
    HORIZONTAL_BORDER = '-'
    EMPTY_CELL        = ' '

    MAX_WIDTH  = 8
    MAX_HEIGHT = 8
    PLAYER_ONE_TOKEN = 'x'
    PLAYER_ONE_QUEEN = 'X'
    PLAYER_TWO_TOKEN = 'o'
    PLAYER_TWO_QUEEN = 'O'

    gameboard = [[EMPTY_CELL for x in range(MAX_WIDTH)] for x in range(MAX_HEIGHT)]

    def __init__(self):
        counter = 0
        for index_row, every_row in enumerate(self.gameboard):
            for index_column, every_column in enumerate(every_row):
                self.gameboard[index_row][index_column] = counter

        print(self.gameboard)

    def print_board(self):
        # clear_terminal()
        for column_index, every_column in enumerate(self.gameboard):
            stdout.write(f'{(" " + (self.HORIZONTAL_BORDER * 3)) * self.MAX_WIDTH}\n')
            stdout.write(f'{self.VERTICAL_BORDER}')
            for row_index, every_cell in enumerate(every_column):
                stdout.write(f' {self.gameboard[column_index][row_index]} |')
            stdout.write(f'\n')
        stdout.write(f'{(" " + (self.HORIZONTAL_BORDER * 3)) * self.MAX_WIDTH}\n')

#DEFINED FUNCTIONS
###################################################################################################
def clear_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

#START PROGRAM
###################################################################################################

def main():
    end_game = False
    my_gameboard = gameboard()
    my_gameboard.print_board()
    while True:
        end_game = True
        if end_game:
            break

#END PROGRAM
main()
