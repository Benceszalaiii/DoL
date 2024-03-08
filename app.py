import fusionengine as fusion
from menu import Menu
from game import Game

class App:

    def __init__(self) -> None:    
        self.main_loop = fusion.Window()
        self.manager = fusion.SceneManager()  
        self.menu = fusion.Scene("menu", Menu)
        self.game = fusion.Scene("game", Game)
        self.manager.add_scene(self.menu)
        self.manager.add_scene(self.game)

        @self.main_loop.loop
        def loop():
            self.manager.start()
            