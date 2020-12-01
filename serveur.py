import socket
import sys
import threading
from constantes import *

hostname = socket.gethostname()
ServIP = socket.gethostbyname(hostname)
print('Ip du Serveur : ', ServIP)


class ThreadClient(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connexion = connection
        self.setName(self.connexion.recv(1024).decode())

    def run(self):
        nom = self.getName()
        while 1:
            msgClient = self.connexion.recv(1024)
            if msgClient == '' or msgClient.upper().decode() == "FIN":
                break
            message = nom + '>' + msgClient.decode()
            print(message)
            for iteration in conn_client:
                if iteration != nom:
                    conn_client[iteration].send(message.encode())

        self.connexion.close()
        del conn_client[nom]
        print("Client", nom, "Déconnecté")


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Actual Connection
try:
    mySocket.bind((ServIP, PORT))
except socket.error:
    print("Mauvais Socket !")
    sys.exit()
mySocket.listen(5)

conn_client = {}  # Liste des connectées
while 1:
    connexion, adresse = mySocket.accept()
    th = ThreadClient(connexion)
    th.start()
    it = th.getName()
    conn_client[it] = connexion
    print("Client", it, "connecté, adresse IP", adresse[0], "port", adresse[1])
    connexion.send("Connection effectué !!".encode())
