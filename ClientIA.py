import socket
from jsonNetwork import sendJSON, receiveJSON

class client():
    def __init__(self, host = socket.gethostname(), port=3000):
        s_client = socket.socket()
        #Accroche le client à une adresse spécifique
        s_client.bind(('localhost',0000))
        self._s= s_client
        #On se connecte au serveur et on envoir une requête
        self._s.connect(('localhost', 3000))
        registration = {
                "request": "subscribe",
                "port": 0000,
                "name": "Hungry Team",
                "matricules": ["195320", "195123"]
        }
        sendJSON(self._s,registration)
        ## On accepte 1 client à la fois. Donc on les met en attente tant qu'un autre est traiter. ##
        ## On commence par écouter ce qu'il se passe. Puis on attend de recevoir une réponse du serveur. ##
        self._s.listen()
        while True:
            try :
                client, addr = self._s.accept()
                req = receiveJSON(3000)
                ## Si on rençoit un ping, on renvoie un pong ##
                if req["request"] == "ping":
                    sendJSON(self._s,{"response": "pong"})
                
                ## Pour les requêtes de jeux: ##
                game_state = {
                    "request": "play",
                    "lives": 3,
                    "errors": list_of_errors,
                    "state": state_of_the_game
                    }   
                while receiveJSON(3000) == game_state:
                    ## Si la fonction minimax nous dit qu'on a une grande probabilité de gagner, on joue. ##
                    my_moves={
                        "response": "move",
                        "move": the_move_played,
                        "message": "Fun message"
                    }
                    ## Si la fonction minimax nous dit qu'on a pas aucune chance de gagner cette partie. ##
                    ## on abandonne ##
                    giveup = {"response": "giveup",}
            ## Ajouter un laps de temps de 3 secondes pour la réponse ##
            except OSError:
                print()

if __name__== "__main__":
    client().run()     
