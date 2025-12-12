import os
from helpers import draw_board, check_side, check_win, format_player, is_available, terminal_colors
from engine import Kibitzer

class Game:
    def __init__(self):
        self.board = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9']
        self.playing = True
        self.won = False
        # Half moves
        self.ply = 0
        self.message = ""
    

def main_menu():
    waiting = True
    while waiting:
        print("Welcome! Please select a game mode from the menu below or press '0' to quit")
        print("     1. Human vs Human")
        print("     2. Human vs AI")
        print("     3. AI vs AI")
        print("     0. Quit game")
        selection = input()
        match selection:
            case '0':
                waiting = False
            case '1':
                human_human()
            case '2':
                human_AI()
            case '3':
                AI_AI()
            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{terminal_colors.FAIL}Invalid option{terminal_colors.END_C}")


def human_human():
    game = Game()

    while game.playing:
        # Reset the screen
        draw_board(game.board)
        print(game.message + f"\nTurn {game.ply + 1} for player {check_side(game.ply)} or press 'q' to quit")
        t0e = Kibitzer()
        t0e.best_move(game.board,game.ply)
        # Get input from player
        move = input()
        if move == 'q':
            game.playing = False
            draw_board(game.board)
            print(f"{terminal_colors.OK_CYAN}{terminal_colors.BOLD}GAME TERMINATED{terminal_colors.END_C}")
        elif str.isdigit(move):
            move_int = int(move) - 1
            if 0 <= move_int < len(game.board):
                # Check if spot is taken
                if is_available(game.board, move_int):
                    # Update board
                    game.board[move_int] = check_side(game.ply)
                    game.ply += 1
                    game.message = ""
                else: game.message = f"{terminal_colors.WARNING}Warning: Spot already taken{terminal_colors.END_C}"
            else: game.message = f"{terminal_colors.FAIL}Invalid move{terminal_colors.END_C}"
        else: game.message = f"{terminal_colors.FAIL}Invalid input{terminal_colors.END_C}"

        if check_win(game.board): game.playing, game.won = False, True
        if game.ply > 8: game.playing = False

    print_end_game(game)

def human_AI():
    game = Game()

    while game.playing:
        # Reset the screen
        draw_board(game.board)
        side = check_side(game.ply)
        print(game.message + f"\nTurn {game.ply + 1} for player {side} or press 'q' to quit")
        if side == 'O':
            t0e = Kibitzer()
            move = t0e.best_move(game.board,game.ply)[0].position
            move_int = int(move) - 1
            if 0 <= move_int < len(game.board):
                # Check if spot is taken
                if is_available(game.board, move_int):
                    # Update board
                    game.board[move_int] = check_side(game.ply)
                    game.ply += 1
                    game.message = ""

            if check_win(game.board): game.playing, game.won = False, True
            if game.ply > 8: game.playing = False
        else: 
            move = input()
            # Get input from player
            if move == 'q':
                game.playing = False
                draw_board(game.board)
                print(f"{terminal_colors.OK_CYAN}{terminal_colors.BOLD}GAME TERMINATED{terminal_colors.END_C}")
            elif str.isdigit(move):
                move_int = int(move) - 1
                if 0 <= move_int < len(game.board):
                    if is_available(game.board, move_int):
                        # Update board
                        game.board[move_int] = side
                        game.ply += 1
                        game.message = ""
                    else: game.message = f"{terminal_colors.WARNING}Warning: Spot already taken{terminal_colors.END_C}"
                else: game.message = f"{terminal_colors.FAIL}Invalid move{terminal_colors.END_C}"
            else: game.message = f"{terminal_colors.FAIL}Invalid input{terminal_colors.END_C}"

        if check_win(game.board): game.playing, game.won = False, True
        if game.ply > 8: game.playing = False

    print_end_game(game)

def AI_AI():
    game = Game()

    while game.playing:
        t0e = Kibitzer()
        move = t0e.best_move(game.board,game.ply)[0].position
        move_int = int(move) - 1
        if 0 <= move_int < len(game.board):
            if is_available(game.board, move_int):
                # Update board
                game.board[move_int] = check_side(game.ply)
                game.ply += 1
                game.message = ""

        if check_win(game.board): game.playing, game.won = False, True
        if game.ply > 8: game.playing = False

    print_end_game(game)

def print_end_game(game: Game):
    draw_board(game.board)
    # Print winner if applicable
    if game.won: print(f"Player '{format_player(check_side(game.ply-1))}' {terminal_colors.OK_GREEN}Wins!{terminal_colors.END_C}")
    else: print(f"{terminal_colors.OK_CYAN}{terminal_colors.BOLD}GAME OVER - Tie!{terminal_colors.END_C}")
