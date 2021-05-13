import socket
from jsonNetwork import sendJSON, receiveJSON
from Strategy import black_strategy, white_strategy
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


def move(move_played, ia):
    my_move = {
        "response": "move",
        "move": move_played,
        "message": "Fun message"
    }
    sendJSON(ia, my_move)


'''
    Statégie en fonction des poins qu'on a
'''


class IAClient:
    def __init__(self, host=socket.gethostname(), port=9000):
        self._s = None
        self._host = host
        self._port = port

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
            except Exception as e:
                pass

    '''
        Pour les requêtes reçu par le serveur
    '''

    def request(self, ia, message):

        if message["request"] == "ping":
            sendJSON(self._s, {"response": "pong"})
            print('answer pong')

        if message["request"] == "play":
            self.play(ia, message)

    '''
        On commence à jouer en mettant en place notre starégie
    '''

    def play(self, ia, message):
        '''
            On commence par récupérer les informations envoyer sur l'état du jeu
        '''
        state = message["state"]
        lives = message["lives"]

        current = message["current"]
        board = state["board"]

        '''
            Si le current est 0, on commence et on a les pions 'B' et inversement
        '''
        if current == 0:
            black_strategy(board ,state)
        else:
            white_strategy(board ,state)

    '''
        Si on décide d'abandonner
    '''

    def give_up(self):
        sendJSON(self._s,{"response": "giveup",})


if __name__ == "__main__":
    IAClient().run()

