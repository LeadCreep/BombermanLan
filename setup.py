# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build
from cx_Freeze import setup, Executable

executables = [
    Executable(script="main.py", base="Win32GUI")
]
# ne pas mettre "base = ..." si le programme n'est pas en mode graphique, comme c'est le cas pour chiffrement.py.

buildOptions = dict(
    includes=["pygame.py"],
    include_files=["fichier1.txt", "mon_icone.ico"]
)

setup(
    name="BoumeurMan",
    version="0.1",
    description="Projet Terminal",
    author="Totor, Morgane, Macéo",
    options=dict(build_exe=buildOptions),
    executables=executables
)
