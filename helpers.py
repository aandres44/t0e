import os

class terminal_colors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def draw_board(board):
    #board = "|1|2|3|\n|4|5|6|\n|7|8|9|"
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, spot in enumerate(board):
        spot = format_player(spot)
        if (i+1) % 3 == 0: print("|" + spot + "|")
        else: print("|" + spot, end="")

def check_side(ply):
    if ply % 2 == 0: return 'O'
    else: return 'X'

def check_win(board):
    # Horizontal
    if      (board[0] == board[1] == board[2]) \
          or (board[3] == board[4] == board[5]) \
          or (board[6] == board[7] == board[8]):
        return True

    # Vertical
    if      (board[0] == board[3] == board[6]) \
          or (board[1] == board[4] == board[7]) \
          or (board[2] == board[5] == board[8]):
        return True

    # Diagonal
    if      (board[0] == board[4] == board[8]) \
          or (board[2] == board[4] == board[6]):
        return True
    else: return False

def format_player(player):
    if player == 'X': player = f"{terminal_colors.OK_BLUE}{player}{terminal_colors.END_C}"
    elif player == 'O': player = f"{terminal_colors.FAIL}{player}{terminal_colors.END_C}"
    return player

def action_for_each(action, action2, board):
    for i, spot in enumerate(board):
        if (i+1) % 3 == 0: action(i, board)
        else: action2(i, spot)

#def validate_move(ply):