from helpers import draw_board, check_side, check_win, format_player, terminal_colors
from engine import best_move

board = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9']

# Give the code more structure
playing = True
won = False

# Half moves
ply = 0

message = ""

def reset_game():
    global board, playing, won, ply, message
    board = ['1', '2', '3', '4' ,'5', '6', '7', '8', '9']

    # Give the code more structure
    playing = True
    won = False

    # Half moves
    ply = 0

    message = ""

def main_menu():
    print("Welcome! Please select a game mode from the menu below or press '0' to quit")
    print("     1. Human vs Human")
    print("     2. Human vs AI")
    print("     3. AI vs AI")
    print("     0. Quit game")

def human_human():
    global board, playing, won, ply, message

    reset_game()

    while playing:
        # Reset the screen
        draw_board(board)
        print(message + f"\nTurn {ply + 1} for player {check_side(ply)} or press 'q' to quit")
        best_move(board,ply)
        # Get input from player
        move = input()
        if move == 'q':
            playing = False
            draw_board(board)
            print(f"{terminal_colors.OK_CYAN}{terminal_colors.BOLD}GAME TERMINATED{terminal_colors.END_C}")
        elif str.isdigit(move):
            move_int = int(move) - 1
            if 0 <= move_int < len(board):
                # Check if spot is taken
                if not board[move_int] in {"X", "O"}:
                    # Update board
                    board[move_int] = check_side(ply)
                    ply += 1
                    message = ""
                else: message = f"{terminal_colors.WARNING}Warning: Spot already taken{terminal_colors.END_C}"
        else: message = f"{terminal_colors.FAIL}Invalid move{terminal_colors.END_C}"

        if check_win(board): playing, won = False, True
        if ply > 8: playing = False

    draw_board(board)

    # Print winner if applicable
    if won: print(f"Player '{format_player(check_side(ply-1))}' {terminal_colors.OK_GREEN}Wins!{terminal_colors.END_C}")
    else: print(f"{terminal_colors.OK_CYAN}{terminal_colors.BOLD}GAME OVER - Tie!{terminal_colors.END_C}")

def human_AI():
    global board, playing, won, ply, message

    reset_game()

    while playing:
        # Reset the screen
        draw_board(board)
        side = check_side(ply)
        print(message + f"\nTurn {ply + 1} for player {side} or press 'q' to quit")
        if side == 'O': 
            move = best_move(board,ply)[0]
            move_int = int(move) - 1
            if 0 <= move_int < len(board):
                # Check if spot is taken
                if not board[move_int] in {"X", "O"}:
                    # Update board
                    board[move_int] = check_side(ply)
                    ply += 1
                    message = ""

            if check_win(board): playing, won = False, True
            if ply > 8: playing = False
        else: 
            move = input()
            # Get input from player
            if move == 'q':
                playing = False
                draw_board(board)
                print(f"{terminal_colors.OK_CYAN}{terminal_colors.BOLD}GAME TERMINATED{terminal_colors.END_C}")
            elif str.isdigit(move):
                move_int = int(move) - 1
                if 0 <= move_int < len(board):
                    # Check if spot is taken
                    if not board[move_int] in {"X", "O"}:
                        # Update board
                        board[move_int] = side
                        ply += 1
                        message = ""
                    else: message = f"{terminal_colors.WARNING}Warning: Spot already taken{terminal_colors.END_C}"
            else: message = f"{terminal_colors.FAIL}Invalid move{terminal_colors.END_C}"

        if check_win(board): playing, won = False, True
        if ply > 8: playing = False

    draw_board(board)

    # Print winner if applicable
    if won: print(f"Player '{format_player(check_side(ply-1))}' {terminal_colors.OK_GREEN}Wins!{terminal_colors.END_C}")
    else: print(f"{terminal_colors.OK_CYAN}{terminal_colors.BOLD}GAME OVER - Tie!{terminal_colors.END_C}")

def AI_AI():

    global board, playing, won, ply, message

    reset_game()

    while playing:
        # Reset the screen
        #draw_board(board)
        #print(message + f"\nTurn {ply + 1} for player {check_side(ply)} or press 'q' to quit")
        move = best_move(board,ply)[0]
    
        move_int = int(move) - 1
        if 0 <= move_int < len(board):
            # Check if spot is taken
            if not board[move_int] in {"X", "O"}:
                # Update board
                board[move_int] = check_side(ply)
                ply += 1
                message = ""

        if check_win(board): playing, won = False, True
        if ply > 8: playing = False

    draw_board(board)

    # Print winner if applicable
    if won: print(f"Player '{format_player(check_side(ply-1))}' {terminal_colors.OK_GREEN}Wins!{terminal_colors.END_C}")
    else: print(f"{terminal_colors.OK_CYAN}{terminal_colors.BOLD}GAME OVER - Tie!{terminal_colors.END_C}")


human_AI()