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
        self.win = fe.Window(TITLE, WIDTH, HEIGHT)
        while True:
            menu = Menu(self.win)
            menu.run()
            # if menu.next == "settings":
            #    settings = Settings(self.win)
            #    settings.run()
            #    continue
            game = Game(self.win)
            game.run()