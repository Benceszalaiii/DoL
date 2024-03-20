# THIS IS THE FILE FOR THE GAME SESSION

# --------- #
#  IMPORTS  #
# --------- #
import pygame as pg
from inputs import global_inputs
import fusionengine as fe
from settings import FPS, WIDTH, HEIGHT, TITLE
import sys
import utils
from player import Player
from destination import Destination
import time


# ------------------- #
#      SESSION        #
# ------------------- #


class Game:

    # ------------------- #
    # INITIALIZE SESSION  #
    # ------------------- #

    # Load all components
    def __init__(self, win):
        self.window_load(win)
        self.characters_load()
        self.animations_load()
        self.pause_load()

# Signal start of game
        print("Switching to game")

# Load window
    def window_load(self, win):
        self.paused: bool = False
        self.window: fe.Window = win
        self.window._running = True

# Load characters and animations
    def characters_load(self):
        self.player: Player = Player(
            self.window, self.window.width, self.window.height, 75, 175)
        self.destination: Destination = Destination(
            self.window, self.player.crect.x, self.player.crect.y, 10, 10)
        self.animations_load()

# Load pause menu
    def pause_load(self):
        self.resume: fe.Button = fe.Button(
            200, 200, 200, 75, 32, "Resume game")

# Load animations -> initialized inside characters_load
    def animations_load(self):
        pass
        # self.ground_arow_sh = fe.SpriteSheet("./ground_arrows.png", 16, 16)
        # self.ground_arrow_an = fe.Animation(self.window, self.ground_arow_sh, 1 / 3)


# ------------------- #
#    START SESSION    #
# ------------------- #


    def run(self):
        self.window.change_icon("logo.png")
        self.bg = fe.Image("background.jpg", 0, 0, WIDTH, HEIGHT)

# ----> GAME LOOP
        @self.window.loop
        def loop():
            self.window.set_fps(FPS)
            self.inputs()
            if self.paused:
                self.pause()
            else:
                self.player.crect.load_rect(fe.ORANGERED)
                self.bg.draw()
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

    def inputs(self):
        global_inputs(self.window)
        if self.paused and self.resume.is_pressed():
            self.paused = False
        if not self.paused and fe.key_down_once(fe.KEY_ESCAPE):
            self.paused = True
        ev = pg.event.get()
        for event in ev:
            if not self.paused and pg.mouse.get_pressed()[0]:
                self.move_player(self.player)
            if event.type == pg.QUIT:
                print("We wish to see you again!")
                sys.exit()

# Calculates the distance and direction on click
    def move_player(self, player: Player):
        dest_x, dest_y = fe.get_mouse_pos(self)
        self.destination.destination.x, self.destination.destination.y = dest_x, dest_y
        self.player.dx = dest_x - player.crect.x
        self.player.dy = dest_y - player.crect.y
        length = max(1, (self.player.dx ** 2 + self.player.dy ** 2) ** 0.5)
        self.player.dx /= length
        self.player.dy /= length

    # ----------------- #
    #    PAUSE MENU     #
    # ----------------- #

    def pause(self) -> None:
        self.resume.draw()
        print("Paused")
