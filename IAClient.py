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


class IAClient:
    def __init__(self, host=socket.gethostname(), port=9800):
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
        Pour écouter sur le certain port défini dans le constructeur
    '''

    def listen(self, host):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._s.bind(('localhost', self._port))
        self._s.listen(5)
        '''backlog of size 5'''
        print('Listening on port {}'.format(self._port))

    '''
        Pour attendre que les clients se connectent et les accepter
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
                self.move(ia, board)
            else:
                self.move(ia, board, False)

    '''
        Pour commencer à jouer et récupéré l'état du jeux, j'appelle la class IAStrategy
    '''

    def play(self, to_move, ia):
        my_move = {
            "response": "move",
            "move": to_move,
            "message": "Pions, attaque tonnerre"
        }
        sendJSON(ia, my_move)

    '''
            On choisit quel move on veut réaliser
        '''

    def move(self, ia, board, black: bool = True):
        self._board = board
        # Those who can be moved classed by direction
        moves = self.get_moves(black)
        partners = self.find_partners(moves)
        count_moves: int = 0
        to_move = {'direction': None, "marbles": None}
        for direction, groups in partners.items():
            for group in groups:
                print(direction)
                print(group)
                if len(group) > count_moves:
                    count_moves = len(group)
                    to_move['direction'] = direction
                    to_move['marbles'] = group

        if to_move['marbles'] and len(to_move['marbles']) > 3:
            to_move['marbles'] = [to_move['marbles'][idx] for idx in range(0, 2)]
        self.play(to_move, ia)
        # TODO Choose which move you have to perform

    def find_partners(self, moves):
        partners = {
            "NE": [],
            "NW": [],
            "E": [],
            "W": [],
            "SW": [],
            "SE": [],
        }
        for direction, marbles in moves.items():
            local_partners = {}
            if marbles and len(marbles) <= 0:
                continue
            for marble in marbles:
                local_partners[marble] = self.can_move_with(marble, marbles)
            partners[direction] = local_partners.values()
        return partners

    def can_move_with(self, key, marbles):
        friends = []
        line, col = key
        friends.append([line, col])
        for marble in marbles:
            x, y = marble
            if line == x and (y == col + 1 or y == col - 1):
                friends.append([x, y])

        return friends

    def get_moves(self, is_black: bool = True):
        me = 'B' if is_black else 'W'
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
                if el != me:
                    continue
                possible_moves = self.possible_moves(ln, col, is_black)
                if possible_moves:
                    for key, value in possible_moves.items():
                        moves[key] += value

        return moves

    def possible_moves(self, line, col, is_black: bool = True):
        possible_moves = {}
        if self.position_empty(line, col - 1):
            possible_moves['W'] = [(line, col)]
        if self.position_empty(line - 1, col - 1) and is_black:
            possible_moves['NW'] = [(line - 1, col)]
        if self.position_empty(line + 1, col) and not is_black:
            possible_moves['SW'] = [(line, col)]
        if self.position_empty(line, col + 1):
            possible_moves['E'] = [(line, col)]
        if self.position_empty(line - 1, col) and is_black:
            possible_moves['NE'] = [(line, col)]
        if self.position_empty(line + 1, col + 1) and not is_black:
            possible_moves['SE'] = [(line, col)]
        return possible_moves

    def position_empty(self, line, col):
        if line < 0 or line >= len(self._board):
            return False
        if col < 0 or col >= len(self._board[line]):
            return False
        return self._board[line][col] == 'E'


if __name__ == "__main__":
    client = IAClient('localhost', 9800)
    client.run()
