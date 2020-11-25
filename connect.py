import socket
import sys
import threading
from tkinter import *
from tkinter.messagebox import *


class BoiteDeDialogue():
    def __init__(self):
        def GetIP():
            self.AdresseIp = self.IP.get()
            print(str(self.AdresseIp))
            self.Mafenetre.destroy()

        # Création de la fenêtre principale (main window)
        self.Mafenetre = Tk()
        self.Mafenetre.title('Identification requise')

        # Création d'un widget Label (texte 'Mot de passe')
        self.Label1 = Label(self.Mafenetre, text='Pseudo')
        self.Label1.pack(side=LEFT, padx=5, pady=5)

        # Création d'un widget Entry (champ de saisie)
        self.IP = StringVar()
        self.Champ = Entry(
            self.Mafenetre, textvariable=self.IP, bg='bisque', fg='maroon')
        self.Champ.focus_set()
        self.Champ.pack(side=LEFT, padx=5, pady=5)

        # Création d'un widget Label (texte 'Mot de passe')
        self.Label1 = Label(self.Mafenetre, text='IP')
        self.Label1.pack(side=RIGHT, padx=5, pady=5)

        # Création d'un widget Entry (champ de saisie)
        self.IP = StringVar()
        self.Champ = Entry(
            self.Mafenetre, textvariable=self.IP, bg='bisque', fg='maroon')
        self.Champ.focus_set()
        self.Champ.pack(side=RIGHT, padx=5, pady=5)

        # Création d'un widget Button (bouton Valider)
        self.Bouton = Button(self.Mafenetre, text='Valider', command=GetIP)
        self.Bouton.pack(side=TOP, padx=5, pady=5)

    def runFenetre(self):
        self.Mafenetre.mainloop()


class ThreadReception(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024)
            print("*" + message_recu.decode() + "*")
            if message_recu == '' or message_recu.upper() == "FIN":
                break

        th_E._Thread__stop()
        print("Connection Rompue")
        self.connexion.close()


class ThreadEmission(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        while 1:
            message_emis = input()
            self.connexion.send(message_emis.encode())

    def envoyer(self, message):
        self.connexion.send(message.encode())


#y = [1, 1, True, 1, 1]
#y = str(y)
# th_E.envoyer(y)
