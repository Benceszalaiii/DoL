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

    play_button: fusion.Button = fusion.Button(533, 300, 533, 600, 50, "Play")

    def __init__(self, win):
        self.win = win
        self.win._running = True
        self.win.set_fps(FPS)
        self.background = fusion.Node(self.win, 0, 0, self.win.width, self.win.height)
        
        #self.settings_button = fusion.Button(533, 600, 533, 25, 50, "Settings")

        print("Welcome to DoL!")

    # def play_button_load(self):
    #    self.play_button: fusion.Button = fusion.Button(200, 200, 200, 75, 32, "Play")

    # def settings_button_load(self):
    #    self.settings_button: fusion.Button = fusion.Button(200, 200, 200, 75, 32, "Settings")

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
            #self.settings_button.draw()
            self.play_button.draw()
            # self.settings_button.draw()

# <---- END OF GAME LOOP

    # ------------------- #
    #       INPUTS        #
    # ------------------- #
# Handle global and sessionwide inputs

    def inputs(self):
        global_inputs(self.win)
