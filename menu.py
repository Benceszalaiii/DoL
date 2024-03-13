import fusionengine as fusion


class Menu:
    menu_scene: fusion.Scene
    
    def __init__(self):
        self.menu_scene = fusion.Scene("DoL", Game)
        self.menu_window = fusion.Window("DoL", 1280, 720)
        
        @self.menu_window.loop
        def loop():
            pass
