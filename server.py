import threading
import sys
import socket
HOST = '172.16.202.102'
PORT = 50000


class ThreadClient(threading.Thread):
    '''dérivation d'un objet thread pour gérer la connexion avec un client'''

    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        nom = self.getName()  # Prendre le nom du client
        while 1:  # Envoi du message
            msgClient = self.connexion.recv(1024)
            if msgClient.upper() == "FIN" or msgClient == "":  # Le client
                break
            message = str(nom + "> " + msgClient.decode())
            print(message)
            for cle in conn_client:
                if cle != nom:
                    conn_client[cle].send(message.encode())

        # Déconnection du client
        self.connexion.close()
        del conn_client[nom]
        print("Client ", nom, " déconnecté.")


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()
print("Serveur prêt, en attente de requêtes ...")
mySocket.listen(5)

conn_client = {}
while 1:
    connexion, adresse = mySocket.accept()
    th = ThreadClient(connexion)
    th.start()
    it = th.getName()
    conn_client[it] = connexion
    print("Client ", (it, adresse[0], adresse[1]), "connecté")
    connexion.send(("Vous êtes connecté. Envoyez vos messages.").encode())
