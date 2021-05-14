import socket
from jsonNetwork import sendJSON, receiveJSON

'''
    On crée un socket client qui va essayer de se connecter au seveur 
    (modèle sensé petre statique, il doit donc être en dehors de la class)
'''


def client_s():
    s_client = socket.socket()
    s_client.connect(('localhost', 3000))
    return s_client


'''
    Pour pouvoir envoyer le mouvement qu'on veut effectuer
'''


class IAClient:
    def __init__(self, host=socket.gethostname(), port=9900):
        self._s = None
        self._host = host
        self._port = port
        self._board = None

    '''
        Pour lancer le programme
    '''

    def run(self):
        self.subscribe()

    '''
        Pour se connecter au serveur.
    '''

    def subscribe(self):
        ia_socket = client_s()
        try:
            '''
                On lance l'inscription et on attend la réponse
            '''
            registration = {
                "request": "subscribe",
                "port": self._port,
                "name": "Hungry Team",
                "matricules": ["195320", "195123"]
            }
            sendJSON(ia_socket, registration)
            message = receiveJSON(ia_socket)
            if message["response"] == "ok":
                self.listen(self._host)
                self.accept()
            else:
                print('Error')

        except OSError:
            print('Connexion avec le serveur non établie')

    '''
        Pour écouter sur un certain port
    '''

    def listen(self, host):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.bind(('localhost', self._port))
        self._s.listen(5)
        '''backlog of size 5'''
        print('Listening on port {}'.format(self._port))

    '''
        Pour attendre que les clients se connecte et les accepter
    '''

    def accept(self):
        print('Waiting for client to connect...')
        while True:
            ia, addr = self._s.accept()
            try:
                message = receiveJSON(ia)
                print('Receiving message from {}'.format(addr))
                self.request(ia, message)

            except OSError:
                pass

    '''
        Pour les requêtes fa
    '''

    def request(self, ia, message):
        if message["request"] == "ping":
            sendJSON(ia, {"response": "pong"})

        if message["request"] == "play":
            print(message["request"])
            state = message['state']
            board = state['board']
            current = state['current']
            if current == 0:
                self.move_black(ia, board)
            else:
                self.move_white(ia, board)

    '''
        Pour commencer à jouer et récupéré l'état du jeux, j'appelle la class IAStrategy
    '''

    def play(self, marble, direction, ia):
        the_move_played = {
            "marbles": marble,
            "direction": direction,
        }
        my_move = {
            "response": "move",
            "move": the_move_played,
            "message": "Pions, attaque tonnerre"
        }
        sendJSON(ia, my_move)

    '''
            On choisit quel move on veut réaliser
        '''

    def move_black(self, ia, board):
        self._board = board
        moves = self.get_moves_black()

        print(moves)
        score = {
            'NE': len(moves['NE']),
            'NW': len(moves['NW']),
            'E': len(moves['E']),
            'W': len(moves['W']),
            'SW': len(moves['SW']),
            'SE': len(moves['SE'])}

        print(score.values())
        v = list(score.values())
        k = list(score.keys())

        direction = k[v.index(max(v))]
        marbles = moves[str(direction)]
        self.move(marbles,direction,ia)


    def move_white(self, ia, board):
        self._board = board
        moves = self.get_moves_white()

        print(moves)
        score = {
            'SE': len(moves['SE']),
            'SW': len(moves['SW']),
            'W': len(moves['W']),
            'E': len(moves['E']),
            'NW': len(moves['NW']),
            'NE': len(moves['NE'])}

        print(score.values())

        v = list(score.values())
        k = list(score.keys())

        direction = k[v.index(max(v))]
        marbles = moves[str(direction)]

        self.move(marbles,direction,ia)

    '''
        On renvoie le mouvement qu'on envera par la suite
    '''
    def move(self,marbles,direction,ia):
        # Je cherche les poins avec ayant la même ligne et ou la même colone

        same_line = []
        same_col = []
        for jj in range(len(marbles) - 1):
            if marbles[jj][0] == marbles[jj + 1][0]:
                same_line.append(marbles[jj])
            if marbles[jj][1] == marbles[jj + 1][1]:
                same_col.append(marbles[jj])
            jj += 1

        print(same_col)
        print(same_line)

        # Je regarde si si sont l'un a coté de l'autre ou pas

        line_aligned = []
        col_aligned = []
        cc = 0
        ll = 0
        for ll in range(len(same_line) - 1):
            if same_line[ll][1] == same_line[ll + 1][1]:
                line_aligned.append(marbles[ll])
            ll += 1
        for cc in range(len(same_col) - 1):
            if marbles[cc][0] == marbles[cc + 1][0]:
                col_aligned.append(same_col[cc])
            cc += 1

        if len(line_aligned) > len(col_aligned):
            my_marbles = line_aligned
        else:
            my_marbles = col_aligned

        print(my_marbles)
        while len(my_marbles) > 3:
            del my_marbles[len(my_marbles) - 1]

        self.play(my_marbles, direction, ia)

    '''
        On met les moves possible dans une liste en fonction de l'état du jeux
    '''

    def get_moves_black(self):
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
                if el != 'B':
                    continue
                possible_moves = self.possible_moves(ln, col)
                if possible_moves:
                    for key, value in possible_moves.items():
                        moves[key] += value

        return moves

    def get_moves_white(self):
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
                if el != 'W':
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
        if self.position_empty(line, col - 1):
            possible_moves['W'] = [[line, col]]
        if self.position_empty(line - 1, col - 1):
            possible_moves['NW'] = [[line - 1, col]]
        if self.position_empty(line + 1, col):
            possible_moves['SW'] = [[line, col]]
        if self.position_empty(line, col + 1):
            possible_moves['E'] = [[line, col]]
        if self.position_empty(line - 1, col):
            possible_moves['NE'] = [[line, col]]
        if self.position_empty(line + 1, col + 1):
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
    IAClient().run()
