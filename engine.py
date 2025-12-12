from helpers import check_side, check_win

class Kibitzer:
    def __init__(self, p1:str='O', p2:str='X'):
        self.p1 = p1
        self.p2 = p2
        self.moves:dict[int, int] = {}
        self.scores = {p1: -1, p2: 1, 'tie': 0}

    def minimax(self, board: list[str], depth: int, is_maximizing: bool, ply: int)->float:
        if check_win(board): return self.scores[check_side(ply)]
        elif ply > 8: return self.scores['tie']

        limit_eval = float('inf')
        player = self.p2
        if is_maximizing: 
            limit_eval = float('-inf')
            player = self.p1
        for i, spot in enumerate(board):
            # Check if the spot is available
            if not spot in {'X', 'O'}:
                board[i] = player
                eval = self.minimax(board, depth + 1, not is_maximizing, ply + 1)
                board[i] = str(i+1)
                #max_eval = max(max_eval, eval)
                if is_maximizing and eval > limit_eval:
                    limit_eval = eval
                    self.moves[depth] = i+1
                elif (not is_maximizing) and eval < limit_eval:
                    limit_eval = eval
                    self.moves[depth] = i+1
        return limit_eval

    def best_move(self, board: list[str], ply: int):
        self.moves = {}
        # p1 to make its turn
        max = False
        if check_side(ply) == 'O': max = True
        print(f"minimax: {self.minimax(board, 0, max, ply)}, best move: {self.moves}")
        return self.moves