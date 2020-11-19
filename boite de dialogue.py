from tkinter import *
from tkinter.messagebox import * # boîte de dialogue

def GetIP():
    AdresseIp = IP.get()
    print(str(AdresseIp))

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Identification requise')

# Création d'un widget Label (texte 'Mot de passe')
Label1 = Label(Mafenetre, text = 'IP')
Label1.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Entry (champ de saisie)
IP = StringVar()
Champ = Entry(Mafenetre, textvariable= IP,bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Label (texte 'Mot de passe')
Label1 = Label(Mafenetre, text = 'Pseudo')
Label1.pack(side = RIGHT, padx = 5, pady = 5)

# Création d'un widget Entry (champ de saisie)
IP = StringVar()
Champ = Entry(Mafenetre, textvariable= IP,bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side = RIGHT, padx = 5, pady = 5)


# Création d'un widget Button (bouton Valider)
Bouton = Button(Mafenetre, text ='Valider', command = GetIP)
Bouton.pack(side = TOP, padx = 5, pady = 5)

Mafenetre.mainloop()