# THIS IS THE FILE FOR THE MENU SESSION
#pylint: disable=too-many-arguments

# --------- #
#  IMPORTS  #
# --------- #


import fusionengine as fe
from inputs import global_inputs
from settings import FPS
from os import system as cmd
from resolutions import Resolution, Screen

# ------------------- #
#       SESSION       #
# ------------------- #

class Menu:

    # ------------------- #
    # INITIALIZE SESSION  #
    # ------------------- #

    def __init__(self, win: fe.Window, screen: Screen):
        self.win = win
        self.win.isrunning = True
        self.screen = screen
        print("Welcome to DoL!")
        self.mode = "main"
        self.startb = fe.Button(self.win.width/2, self.win.height/2, 200, 100, 24, "Start game")
        self.background = fe.Node(self.win, 0, 0, self.screen.current.width, self.screen.current.height)
        self.curr_resized: bool = False
        self.win.change_icon("logo.png")

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
                self.background.load_image("menu_background.jpg")
                self.background.update()
                self.startb.draw()
                self.inputs()

# <---- END OF GAME LOOP

    # ------------------- #
    #       INPUTS        #
    # ------------------- #
# Handle global and sessionwide inputs
    def inputs(self):
        global_inputs(self.win)
        self.handle_resolution()
    def handle_resolution(self):
        if fe.key_down_once(fe.KEY_2) and self.screen.current.as_str != "1280x720":
            self.swap_resolution(Resolution(1280, 720))
            self.refresh_after_change()
        if fe.key_down_once(fe.KEY_1) and self.screen.current.as_str != "1600x900":
            self.swap_resolution(Resolution(1600, 900))
            self.refresh_after_change()

    def refresh_after_change(self):
        self.background.width, self.background.height, self.background.x, self.background.y = self.screen.current.width, self.screen.current.height, 0, 0
        cmd("cls")
        print("Resizing..")
        self.curr_resized = False

    def swap_resolution(self, new_res: Resolution):
        self.win.resize(new_res)
        self.res = new_res.as_str
        self.screen.current = new_res
        self.curr_resized = True
