import fusionengine as fusion
from settings import TITLE, FPS, WIDTH, HEIGHT
import pygame as pg
import sys
class Menu:
    def __init__(self, win):
        self.win = win
        self.win._running = True
        self.win.set_fps(FPS)
        self.background = fusion.Node(self.win, 0, 0, self.win.width, self.win.height)
        print("Welcome to DoL!")
    def run(self):
        @self.win.loop
        def loop():
            self.win.change_icon("logo.png")
            self.background.load_image("menu_background.jpg")
            ev = pg.event.get()
            for event in ev:
                if event.type == pg.QUIT:
                    print("We wish to see you again!")
                    sys.exit()
            if fusion.key_down_once(fusion.KEY_ESCAPE):
                self.win.quit()
            self.background.update()