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
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connexion = connection
        self.setName(self.connexion.recv(1024).decode())
        self.nom = self.getName()

    def run(self):
        while 1:
            try:
                self.msgClient = self.connexion.recv(1024).decode()
                if self.msgClient == '' or self.msgClient.upper() == "FIN":
                    break
                message = json.loads(self.msgClient)
                #print(self.nom, "MsgClient : ", self.msgClient)
                #print(self.nom, "message :", message)
                self.envoyer(json.dumps(message))
            except json.decoder.JSONDecodeError:
                print("[", str(datetime.now()), "]", "Packet Lost")

        self.connexion.close()
        del conn_client[self.nom]
        print("[", str(datetime.now()), "]", "Client", self.nom, "Déconnecté")

    def envoyer(self, message):
        for iteration in conn_client:
            if iteration != self.nom:
                conn_client[iteration].send(self.msgClient.encode())


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
while 1:
    connexion, adresse = mySocket.accept()
    th = ThreadClient(connexion)
    th.start()
    it = th.getName()
    conn_client[it] = connexion
    print("[", str(datetime.now()), "]", "Client", it,
          "connecté, adresse IP", adresse[0], "port", adresse[1])
