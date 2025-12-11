from helpers import check_side, check_win, action_for_each

class Kibitzer:
    def __init__(self, p1='O', p2='X'):
        self.p1 = p1
        self.p2 = p2
        self.moves = {}
        self.scores = {p2: 1, p1: -1, 'tie': 0}

    def minimax(self, board, depth, is_maximizing, ply):
        if check_win(board): return self.scores[check_side(ply)]
        elif ply > 8: return self.scores['tie']
        
        if is_maximizing:
            max_eval = float('-inf')
            for i, spot in enumerate(board):
                # Check if the spot is available
                if not spot in {'X', 'O'}:
                    board[i] = self.p1
                    eval = self.minimax(board, depth + 1, False, ply + 1)
                    board[i] = str(i+1)
                    #max_eval = max(max_eval, eval)
                    if eval > max_eval:
                        max_eval = eval
                        self.moves[depth] = i+1
            return max_eval
            #move = {}
        else:
            min_eval = float('inf')
            for i, spot in enumerate(board):
                # Check if the spot is available
                if not spot in {'X', 'O'}:
                    board[i] = self.p2
                    eval = self.minimax(board, depth + 1, True, ply + 1)
                    board[i] = str(i+1)
                    #min_eval = min(min_eval, eval)
                    if eval < min_eval:
                        min_eval = eval
                        self.moves[depth] = i+1    
            return min_eval
            # Check if the spot is available
            #action_for_each(check_available, board=board)
    def best_move(self, board, ply):
        self.moves = {}
        # p1 to make its turn
        # use another parameter to track the best move and return it here
        max = False
        if check_side(ply) == 'O': max = True
        print(f"minimax: {self.minimax(board, 0, max, ply)}, best move: {self.moves}")
        return self.moves

"""def check_available(i, board):
    if not board[i] in {"X", "O"}:
        board[i] = p1
        score = minimax(board, depth + 1, False, ply + 1)"""