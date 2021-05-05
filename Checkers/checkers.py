'''
checkers.py

simple checkers game.
'''
#REQUIRED LIBRARIES
###################################################################################################
from sys import stdout
from os import system, name

#OBJECTS/CLASSES
###################################################################################################

class game_state:
    end_game    = None
    player_turn = None

class token:
    HIGHLIGHT      = '> <'
    ROW            = None
    COLUMN         = None
    player_control = None
    neighbors      = []
    selected       = None

    def __init__(self):
        return

class gameboard:
    VERTICAL_BORDER   = '|'
    HORIZONTAL_BORDER = '-'
    EMPTY_CELL        = ' '
    MAX_WIDTH         = 8
    MAX_HEIGHT        = 8
    PLAYER_ONE_TOKEN  = 'x'
    PLAYER_ONE_QUEEN  = 'X'
    PLAYER_TWO_TOKEN  = 'o'
    PLAYER_TWO_QUEEN  = 'O'
    highlighted_token = (0, 0)
    gameboard         = None

    def __init__(self):
        # Initialize board with spaces
        self.gameboard = [[self.EMPTY_CELL for x in range(self.MAX_WIDTH)] for x in range(self.MAX_HEIGHT)]

        for index_row, every_row in enumerate(self.gameboard):
            for index_column, every_column in enumerate(every_row):
                # If we are on Player Two side,
                if index_row <= 2:
                    # For every cell in index_row,
                    for every_cell in range(len(every_row)):
                        # If we are in an Odd Row,
                        if index_row % 2:
                            # If we are in an Odd Cell,
                            if not every_cell % 2:
                                self.gameboard[index_row][every_cell] = self.PLAYER_TWO_TOKEN
                        else:
                            # If we are in an Even Cell,
                            if every_cell % 2:
                                self.gameboard[index_row][every_cell] = self.PLAYER_TWO_TOKEN

                # If we are on Player One side,
                elif index_row >= 5:
                    # For every cell in index_row,
                    for every_cell in range(len(every_row)):
                        # If we are in an Odd Row,
                        if index_row % 2:
                            # If we are in an Odd Cell,
                            if not every_cell % 2:
                                self.gameboard[index_row][every_cell] = self.PLAYER_ONE_TOKEN
                        else:
                            # If we are in an Even Cell,
                            if every_cell % 2:
                                self.gameboard[index_row][every_cell] = self.PLAYER_ONE_TOKEN

        return

    def print_board(self):
        clear_terminal()
        for column_index, every_column in enumerate(self.gameboard):
            stdout.write(f'{(" " + (self.HORIZONTAL_BORDER * 3)) * self.MAX_WIDTH}\n')
            stdout.write(f'{self.VERTICAL_BORDER}')
            for row_index, every_cell in enumerate(every_column):
                stdout.write(f' {self.gameboard[column_index][row_index]} |')
            stdout.write(f'\n')
        stdout.write(f'{(" " + (self.HORIZONTAL_BORDER * 3)) * self.MAX_WIDTH}\n')
        return

#DEFINED FUNCTIONS
###################################################################################################
def clear_terminal():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def select_token(given_gameboard, given_input):
    stdout.write(f'FROM select_token given_input = {given_input}\n')
    input()
    if given_gameboard is None or given_input is None:
        return False

    given_gameboard.print_board()
    return True

def update_board(given_gameboard, given_player, given_move):
    return True

def request_selection(given_game_state):
    stdout.write(f'{given_game_state.player_turn}, please select checker to move. (W, A, S, D)\n')
    player_move = ' '
    while not player_move in 'wasdWASD':
        player_move = input()
    return player_move

def main():
    this_game_state = game_state()
    this_game_state.end_game = False
    my_gameboard = gameboard()
    my_gameboard.print_board()
    while True:
        this_game_state.player_control = 'Player 1'
        player_input = request_selection(this_game_state)
        while not select_token(my_gameboard, player_input):
            player_input = request_selection(this_game_state)

        end_game = True
        if end_game:
            break

#START PROGRAM
###################################################################################################

main()

#END PROGRAM
