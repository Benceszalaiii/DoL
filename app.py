import fusionengine as fusion
from menu import Menu
from game import Game
from settings import FPS, WIDTH, HEIGHT, TITLE


class App:

    def __init__(self) -> None:
        self.main_loop = fusion.Window(TITLE, WIDTH, HEIGHT)
        self.main_loop.set_fps(FPS)
        self.manager = fusion.SceneManager(self.main_loop)
        self.menu = fusion.Scene("menu", Menu)
        self.game = fusion.Scene("game", Game)
        self.manager.add_scene(self.menu)
        self.manager.add_scene(self.game)

        @self.main_loop.loop
        def loop():
            self.manager.start()
