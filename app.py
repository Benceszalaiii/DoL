# THIS IS THE FILE FOR SESSION MANAGEMENT

# ----------- #
#   IMPORTS   #
# ----------- #
from os import system as cmd
import fusionengine as fe
from menu import Menu
from game import Game
from settings import FPS, TITLE, WIDTH, HEIGHT
from resolutions import Screen

# ----------------- #
#  SESSION MANAGER  #
# ----------------- #

class App:
    def __init__(self) -> None:
        self.screen = Screen()
        self.win: fe.Window = fe.Window(TITLE, self.screen.current.width, self.screen.current.height)
        while True:
            menu = Menu(self.win, self.screen)
            menu.run()
            self.win.resize(menu.screen.current)
            cmd("cls")
            game = Game(self.win)
            game.run()
            cmd("cls")
