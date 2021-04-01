
from cx_Freeze import setup, Executable

# On appelle la fonction setup

buildOptions = dict(
    includes=["pygame.py"],
    include_files=["fichier1.txt", "mon_icone.ico"]
)

setup(
    name="BoumeurMan",
    version="1",
    description="Projet Terminale 2021",
    executables=[Executable("main.py")],
)
