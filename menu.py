import fusionengine as fusion


class Menu:
    menu_scene: fusion.Scene
    something: fusion.Node 
    def __init__(self, window: fusion.Window):
        self.win = window
        self.something = fusion.Node(window, 150, 150, 150, 150)
        self.something.load_image(fusion.DEBUGIMAGE)
        print("Welcome to DoL!")
        @self.win.loop
        def loop():
            self.something.update()
            print("Az armin buzi")
            if fusion.key_down_once(fusion.KEY_ESCAPE):
                self.win.quit()