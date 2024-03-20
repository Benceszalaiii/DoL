# THIS IS THE FILE FOR THE MENU SESSION

# --------- #
#  IMPORTS  #
# --------- #

import fusionengine as fusion
from settings import TITLE, FPS, WIDTH, HEIGHT
import pygame as pg
import sys
from inputs import global_inputs


# ------------------- #
#       SESSION       #
# ------------------- #

class Menu:

    # ------------------- #
    # INITIALIZE SESSION  #
    # ------------------- #

    def __init__(self, win):
        self.win = win
        self.win._running = True
        self.win.set_fps(FPS)
        self.background = fusion.Node(self.win, 0, 0, self.win.width, self.win.height)
        print("Welcome to DoL!")

    # ------------------- #
    #    START SESSION    #
    # ------------------- #

    def run(self):

        @self.win.loop
        def loop():
            self.win.change_icon("logo.png")
            self.background.load_image("menu_background.jpg")
            self.inputs()
            self.background.update()

# <---- END OF GAME LOOP

    # ------------------- #
    #       INPUTS        #
    # ------------------- #
# Handle global and sessionwide inputs

    def inputs(self):
        global_inputs(self.win)
