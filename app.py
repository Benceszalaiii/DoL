# THIS IS THE FILE FOR SESSION MANAGEMENT

# ----------- #
#   IMPORTS   #
# ----------- #

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
        self.win.set_fps = FPS
        while True:
            menu = Menu(self.win)
            menu.run()
            game = Game(self.win)
            game.run()
