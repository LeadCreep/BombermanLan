import json
import threading
from tkinter import LEFT, RIGHT, TOP, Button, Entry, Label, StringVar, Tk


class BoiteDeDialogue():
    def __init__(self):
        self.nom = None
        self.AdresseIp = None

        def GetIP():
            self.AdresseIp = self.IP.get()
            print(str(self.AdresseIp))
            self.nom = self.Pseudo.get()
            print(str(self.nom))
            self.Mafenetre.destroy()

        # Création de la fenêtre principale (main window)
        self.Mafenetre = Tk()
        self.Mafenetre.title('Identification requise')

        # Création d'un widget Label (texte 'Mot de passe')
        self.Label1 = Label(self.Mafenetre, text='Pseudo')
        self.Label1.pack(side=LEFT, padx=5, pady=5)

        # Création d'un widget Entry (champ de saisie)
        self.Pseudo = StringVar()
        self.Champ = Entry(
            self.Mafenetre, textvariable=self.Pseudo, bg='bisque', fg='maroon')
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
        self.message_recu = None
        self.message = "MessageBase"

    def run(self):
        while 1:
            try:
                self.message_recu = self.connexion.recv(1024)
                self.message = json.loads(self.message_recu)
            except json.decoder.JSONDecodeError:
                print("PacketLost!")

        self._Thread__stop()
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
        try:
            self.connexion.send(message.encode())
        except AttributeError:
            print("NoneType !")


#y = [1, 1, True, 1, 1]
#y = str(y)
# th_E.envoyer(y)
