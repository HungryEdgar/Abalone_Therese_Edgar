from jsonNetwork import receiveJSON,sendJSON
class Strategy:

    def __init__(self, black: bool = True):
        self._board = None
        self._type: bool = black
        self._me = 'B' if black else 'W'
        self._adversary = 'W' if not black else 'B'

    '''
        On choisit quel move on veut réaliser
    '''

    def move(self, board):
        self._board = board
        moves = self.get_moves()
        print(moves)
        # TODO Choose which move you have to perform

    '''
        On met les moves possible dans une liste en fonction de l'état du jeux
    '''

    def get_moves(self):
        moves = {
            "NE": [],
            "NW": [],
            "E": [],
            "W": [],
            "SW": [],
            "SE": [],
        }
        for ln, line in enumerate(self._board):
            for col, el in enumerate(line):
                if el != self._me:
                    continue
                possible_moves = self.possible_moves(ln, col)
                if possible_moves:
                    for key, value in possible_moves.items():
                        moves[key] += value

        return moves

    '''
        Pour avoir les moves possibles
    '''

    def possible_moves(self, line, col):
        possible_moves = {}
        if self.position_empty(line, col-1):
            possible_moves['W'] = [[line, col]]
        if self.position_empty(line-1, col-1):
            possible_moves['NW'] = [[line-1, col]]
        if self.position_empty(line+1, col):
            possible_moves['SW'] = [[line, col]]
        if self.position_empty(line, col+1):
            possible_moves['E'] = [[line, col]]
        if self.position_empty(line-1, col):
            possible_moves['NE'] = [[line, col]]
        if self.position_empty(line+1, col+1):
            possible_moves['SE'] = [[line, col]]
        return possible_moves

    '''
        Pour avoir les positions vides
    '''

    def position_empty(self, line, col):
        if line < 0 or line >= len(self._board):
            return False
        if col < 0 or col >= len(self._board[line]):
            return False
        return self._board[line][col] == 'E'


if __name__ == "__main__":
    strategy = Strategy()
    strategy.move([
      ["W", "W", "W", "W", "W", "X", "X", "X", "X"],
      ["W", "W", "W", "W", "W", "W", "X", "X", "X"],
      ["E", "E", "W", "W", "W", "E", "E", "X", "X"],
      ["E", "E", "E", "E", "E", "E", "E", "E", "X"],
      ["E", "E", "E", "E", "E", "E", "E", "E", "E"],
      ["X", "E", "E", "E", "E", "E", "E", "E", "E"],
      ["X", "X", "E", "E", "B", "B", "B", "E", "E"],
      ["X", "X", "X", "B", "B", "B", "B", "B", "B"],
      ["X", "X", "X", "X", "B", "B", "B", "B", "B"]
   ])
