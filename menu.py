# THIS IS THE FILE FOR THE MENU SESSION
#pylint: disable=too-many-arguments

# --------- #
#  IMPORTS  #
# --------- #

import fusionengine as fe
from inputs import global_inputs
from settings import FPS
from os import system as cmd

# ------------------- #
#       SESSION       #
# ------------------- #

class Menu:

    # ------------------- #
    # INITIALIZE SESSION  #
    # ------------------- #

    def __init__(self, win: fe.Window):
        self.win = win
        self.win.isrunning = True
        self.win._fps = 60
        print("Welcome to DoL!")
        self.mode = "main"
        self.startb = fe.Button(self.win.width/2, self.win.height/2, 200, 100, 24, "Start game")
        self.bg = fe.Image("menu_background.jpg", 0, 0, self.win.width, self.win.height)
        self.elements = (self.bg, self.startb)
        self.curr_resized: bool = False
        self.res =
    # ------------------- #
    #    START SESSION    #
    # ------------------- #

    def run(self):
        @self.win.loop # type: ignore
        def loop():
            if self.mode == "settings":
                # Settings menu
                pass
            elif self.mode == "main":
                if self.curr_resized:
                    cmd("cls")
                    print("Resizing..")
                    self.refresh_after_change()
                    self.curr_resized = False
                # Main Menu
                self.win.change_icon("logo.png")
                self.bg.draw()
                self.startb.draw()
                self.inputs()

# <---- END OF GAME LOOP

    # ------------------- #
    #       INPUTS        #
    # ------------------- #
# Handle global and sessionwide inputs
    def refresh_after_change(self):
        self.bg.width = self.win.width
        self.bg.height = self.win.height
    def inputs(self):
        global_inputs(self.win)
        if self.startb.is_pressed() and self.res == "1600x900":
            self.win.resize((1000, 1000))
            self.res = "1000x1000"
            self.curr_resized = True
        elif self.startb.is_pressed() and self.res == "1000x1000":
            self.win.resize((1600, 900))
            self.res = "1600x900"
            self.curr_resized = True
