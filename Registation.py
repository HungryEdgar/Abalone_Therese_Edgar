import socket
#importons la fonction sendJSON préalablement créée
from jsonNetwork import sendJSON
server.py
s = socket.socket()

#Pour se connecter au serveur
#Si tout est ok
try:
    s.connect("www.gloogle.be", 8888) 
    registration = {
      "request": "subscribe",
      "port": 8888,
      "name": "Hungry Team",
      "matricules": ["195320", "195123"]
    sendJSON(s,registration)
      
    no_error = { 
      "response": "ok"}
    sendJSON(s,no_error)
#Si il y a une erreure
except OSError:
    error = {
      "response": "error",
      "error": "error message"}
    sendJSON(s,error)
