import fusionengine as fusion
from menu import Menu
from game import Game
from settings import FPS, TITLE, WIDTH, HEIGHT
class App:
    def __init__(self) -> None:
        self.win = fusion.Window(TITLE, WIDTH, HEIGHT)
        while True:
            menu = Menu(self.win)
            menu.run()
            game = Game(self.win)
            game.run()