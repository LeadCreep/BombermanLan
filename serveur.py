import json
import socket
import sys
import threading
from datetime import datetime

from constantes import PORT

hostname = socket.gethostname()
ServIP = socket.gethostbyname(hostname)
print("[", str(datetime.now()), "]", 'Ip du Serveur : ', ServIP)


class ThreadClient(threading.Thread):
    def __init__(self, connection, numJoueur):
        threading.Thread.__init__(self)
        self.numJoueur = numJoueur
        self.connexion = connection
        self.setName(self.connexion.recv(16394).decode())
        self.nom = self.getName()

    def run(self):
        while 1:
            try:
                self.msgClient = self.connexion.recv(16394).decode()
                if self.msgClient == '' or self.msgClient.upper() == "FIN":
                    break
                message = json.loads(self.msgClient)
                message.append(self.numJoueur)
                self.partager(json.dumps(message))
            except json.decoder.JSONDecodeError:
                print("[", str(datetime.now()), "]", "Packet Lost")

        self.connexion.close()
        del conn_client[self.nom]
        print("[", str(datetime.now()), "]", "Client", self.nom, "Déconnecté")

    def partager(self, message):
        for iteration in conn_client:
            if iteration != self.nom:
                conn_client[iteration].send(message.encode())


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Actual Connection
try:
    mySocket.bind((ServIP, PORT))
except socket.error:
    print("[", str(datetime.now()), "]", "Mauvais Socket !")
    input("Appuiyer sur une touche pour continuer...")
    sys.exit()
mySocket.listen(5)

conn_client = {}  # Liste des connectées
numJoueur = 0
while 1:
    connexion, adresse = mySocket.accept()
    numJoueur += 1
    th = ThreadClient(connexion, numJoueur)
    th.start()
    it = th.getName()
    conn_client[it] = connexion
    print("[", str(datetime.now()), "]", "Client", it,
          "connecté, adresse IP", adresse[0], "port", adresse[1], "Joueur : ", th.numJoueur)
