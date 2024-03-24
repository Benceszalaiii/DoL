# THIS IS THE FILE FOR THE GAME SESSION
#pylint: disable=too-many-arguments

# --------- #
#  IMPORTS  #
# --------- #

import sys
from os import system as cmd
import pygame as pg
from handler import Handler
import fusionengine as fe
from destination import Destination
from inputs import global_inputs
from player import Player
from resolutions import Screen
from utils import empty_terminal

# ------------------- #
#      SESSION        #
# ------------------- #


class Game:

    # -------------------- #
    #  INITIALIZE SESSION  #
    # -------------------- #

    # Load all components
    def __init__(self, win, screen, game_state):
        self.win = win
        self.screen = screen
        self.paused = False
        self.characters_load()
        self.animations_load()
        self.pause_load()
        self.bg = fe.Image("background.jpg", 0, 0, self.win.width, self.win.height)

        # Signal start of game
        empty_terminal()
        print("Have fun playing!")
        print(

"     *******       *******",
"   **********     *********",
"  *************  ***********",
" ****************************",
"******************************",
" ****************************",
"  **************************",
"    **********************",
"      ******************",
"        *************",
"          **********",
"            ******",
"              **", sep="\n")


    # Load characters and animations
    def characters_load(self):
        self.player: Player = Player(
            self.win, self.win.width, self.win.height, 75, 175)
        self.destination: Destination = Destination(
            self.win, self.player.crect.x, self.player.crect.y, 10, 10)
        self.animations_load()
        

    # Load pause menu
    def pause_load(self):
        self.resume: fe.Button = fe.Button(200, 200, 100, 60, 32, "Resume game")
        self.resume.set_button_color(fe.RED)
        self.resume.set_text_color(fe.WHITE)
        
    # Load animations -> initialized inside characters_load
    def animations_load(self):
        pass
        # self.ground_arow_sh = fe.SpriteSheet("./ground_arrows.png", 16, 16)
        # self.ground_arrow_an = fe.Animation(self.win, self.ground_arow_sh, 1 / 3)

    # ------------------- #
    #    START SESSION    #
    # ------------------- #

    def run(self, game_state):
        
        # ----> GAME LOOP
            self.inputs(game_state)
            if self.paused:
                self.pause()
            else:
                self.bg.draw()
                self.player.crect.load_rect(fe.ORANGERED)
                self.player.load_rect(fe.WHITE)
                self.destination.load_rect(fe.PINK)
                # self.destination_rect.load_animation(self.ground_arrow_an)
                self.player.update(self.destination)
                self.destination.update()

    # <---- END OF GAME LOOP

    # ----------------- #
    # MOVEMENT / INPUT  #
    # ----------------- #

    # Handles global and sessionwide inputs

    def inputs(self, game_state):
        global_inputs()
        if fe.key_down_once(fe.KEY_TAB):
            game_state = "menu"
        if self.paused and self.resume.is_pressed():
            empty_terminal()
            print("Have fun playing!")
            self.paused = False
        if not self.paused and fe.key_down_once(fe.KEY_ESCAPE):
            self.paused = True
            empty_terminal()
            print("Paused")
        ev = pg.event.get()
        for event in ev:
            if not self.paused and pg.mouse.get_pressed()[0]:
                self.move_player(self.player)
            if event.type == pg.QUIT:
                empty_terminal()
                print("We wish to see you again!")
                sys.exit()

    # Calculates the distance and direction on click
    def move_player(self, player: Player):
        dest_x, dest_y = fe.get_mouse_pos(self)
        self.destination.destination.x, self.destination.destination.y = dest_x, dest_y
        self.player.dx = float(dest_x - player.crect.x)
        self.player.dy = float(dest_y - player.crect.y)
        length = max(1, (self.player.dx ** 2 + self.player.dy ** 2) ** 0.5)
        self.player.dx /= length
        self.player.dy /= length

    # ----------------- #
    #    PAUSE MENU     #
    # ----------------- #
    
    # Handles pause (game loop update)
    def pause(self) -> None:
        self.resume.draw()
