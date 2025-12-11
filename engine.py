from helpers import check_side, check_win, action_for_each

scores = {'X': 1, 'O': -1, 'tie': 0}

p1 = 'O'
p2 = 'X'
moves = {}

def best_move(board, ply):
    global moves
    moves = {}
    # p1 to make its turn
    # use another parameter to track the best move and return it here
    max = False
    if check_side(ply) == 'O': max = True
    print(f"minimax: {minimax(board, 0, max, ply)}, best move: {moves}")
    return moves


def minimax(board, depth, is_maximizing, ply):
    global moves
    if check_win(board): return scores[check_side(ply)]
    elif ply > 8: return scores['tie']
    
    if is_maximizing:
        max_eval = float('-inf')
        for i, spot in enumerate(board):
            # Check if the spot is available
            if not spot in {'X', 'O'}:
                board[i] = p1
                eval = minimax(board, depth + 1, False, ply + 1)
                board[i] = str(i+1)
                #max_eval = max(max_eval, eval)
                if eval > max_eval:
                    max_eval = eval
                    moves[depth] = i+1
        return max_eval
        #move = {}
    else:
        min_eval = float('inf')
        for i, spot in enumerate(board):
            # Check if the spot is available
            if not spot in {'X', 'O'}:
                board[i] = p2
                eval = minimax(board, depth + 1, True, ply + 1)
                board[i] = str(i+1)
                #min_eval = min(min_eval, eval)
                if eval < min_eval:
                    min_eval = eval
                    moves[depth] = i+1
                    
        return min_eval



        # Check if the spot is available
        #action_for_each(check_available, board=board)

"""def check_available(i, board):
    if not board[i] in {"X", "O"}:
        board[i] = p1
        score = minimax(board, depth + 1, False, ply + 1)"""