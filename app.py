# THIS IS THE FILE FOR SESSION MANAGEMENT

# ----------- #
#   IMPORTS   #
# ----------- #
from os import system as cmd
import fusionengine as fe
from menu import Menu
from game import Game
from settings import FPS, TITLE, WIDTH, HEIGHT


# ----------------- #
#  SESSION MANAGER  #
# ----------------- #

class App:
    def __init__(self) -> None:
        self.win: fe.Window = fe.Window(TITLE, WIDTH, HEIGHT)
        self.win.fps = FPS
        while True:
            menu = Menu(self.win)
            menu.run()
            cmd("cls")
            game = Game(self.win)
            game.run()
            cmd("cls")
