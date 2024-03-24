# THIS IS THE FILE FOR THE MENU SESSION
#pylint: disable=too-many-arguments

# --------- #
#  IMPORTS  #
# --------- #

import pygame as pg
import fusionengine as fe
from inputs import global_inputs
from utils import empty_terminal
from resolutions import Resolution


# ------------------- #
#       SESSION       #
# ------------------- #

class Menu:

    # ------------------- #
    # INITIALIZE SESSION  #
    # ------------------- #

    def __init__(self, window: fe.Window, screen):
        self.screen = screen
        print("Welcome to DoL!")
        self.win: fe.Window = window
        self.startb = fe.Button(self.screen.current.width/2, self.screen.current.height/2, 200, 100, 24, "Start game")
        self.background = fe.Node(self.win, self.screen.offset_x, self.screen.offset_y, self.screen.current.width, self.screen.current.height)
        self.bg = pg.image.load("menu_background.jpg")
        self.state = "main"
        self.cooldown = False

    # ------------------- #
    #    START SESSION    #
    # ------------------- #

    def run(self, game_state):
# ----> START OF GAME LOOP
        if self.state == "settings":
            empty_terminal()
            print("Settings")
            # Settings menu
            pass
        elif self.state == "main":
            # Main Menu
            self.background.load_image("menu_background.jpg")
            self.background.update()
            self.startb.draw()
            self.inputs(game_state)

# <---- END OF GAME LOOP

    # ------------------- #
    #       INPUTS        #
    # ------------------- #
# Handle global and sessionwide inputs
    def inputs(self, game_state):
        global_inputs()
        self.handle_resolution()
        if self.startb.is_pressed() and not self.cooldown:
            game_state = "game"
            self.cooldown = True


    def handle_resolution(self):
        if fe.key_down_once(fe.KEY_2) and self.screen.current.as_str != "1280x720":
            self.swap_resolution(Resolution(1280, 720))
        if fe.key_down_once(fe.KEY_1) and self.screen.current.as_str != "1600x900":
            self.swap_resolution(Resolution(1600, 900))
        if fe.key_down_once(fe.KEY_3) and self.screen.current.as_str != "800x600":
            self.swap_resolution(Resolution(1900, 1060))

    def refresh_after_change(self):
        self.background.width  = self.screen.current.width
        self.background.height = self.screen.current.height
        self.background.x = self.offset_x
        self.background.y = self.offset_y
        empty_terminal()
        print("Resizing..")

    def swap_resolution(self, new_res: Resolution):
        self.win.resize(new_res)
