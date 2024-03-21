# THIS IS THE FILE FOR THE MENU SESSION

# --------- #
#  IMPORTS  #
# --------- #

import fusionengine as fe
from inputs import global_inputs
from settings import FPS


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
        self.win.set_fps(FPS)
        self.background = fe.Node(self.win, 0, 0, self.win.width, self.win.height)
        print("Welcome to DoL!")
        self.mode = "main"

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
                # Main Menu
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
