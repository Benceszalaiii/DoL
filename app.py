import fusionengine as fusion
from menu import Menu
from game import Game
from settings import FPS, TITLE

class App:

    def __init__(self) -> None:
        self.main_loop = fusion.Window(TITLE, 1280, 720)
        self.main_loop.set_fps(FPS)
        self.manager = fusion.SceneManager(self.main_loop)
        self.menu = fusion.Scene("menu", Menu, self.main_loop)
        self.game = fusion.Scene("game", Game, self.main_loop)
        self.manager.add_scene(self.menu)
        self.manager.add_scene(self.game)
        self.manager.start()