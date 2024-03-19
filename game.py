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



# ------------------- #
#      SESSION        #
# ------------------- # 


class Game:


# ------------------- # 
# INITIALIZE SESSION  #
# ------------------- # 

    def __init__(self, win):
        self.window: fe.Window = win
        self.window._running = True
        self.p_speed: int = 5
        self.player = Player(self.window, self.window.width, self.window.height, 75, 175)
        self.dx: float = 0
        self.dy: float = 0

        self.destination: fe.Node = fe.Node(self.window, self.player_f.x, self.player_f.y, 10, 10)
        self.destination_rect = pg.Rect(self.destination.x, self.destination.y, self.destination.width, self.destination.height)
        self.ground_arow_sh = fe.SpriteSheet("./ground_arrows.png", 16, 16)
        self.ground_arrow_an = fe.Animation(self.window, self.ground_arow_sh, 1 / 3)
        print("Switching to game")


# ------------------- # 
#    START SESSION    # 
# ------------------- #

    def run(self):
        self.window.change_icon("logo.png")
        self.bg = fe.Image("background.jpg", 0, 0, WIDTH, HEIGHT)
        
        
        @self.window.loop
        def loop():
            self.player_f.load_rect(fe.ORANGERED)
            self.window.set_fps(FPS)
            self.bg.draw()
            self.player.load_rect( fe.WHITE)
            self.destination.load_rect( fe.PINK)
                #self.destination_rect.load_animation(self.ground_arrow_an)
            self.player.update()
            self.player_f.update()
            self.inputs()
            self.walk()
            self.player_rect.update(self.player_f.x, self.player_f.y, self.player_f.width, self.player_f.height)
            self.destination_rect.update(self.destination.x, self.destination.y, self.destination.width, self.destination.height)
            self.player.x = self.player_f.x - self.player.width/2
            self.player.y = self.player_f.y - self.player.height/2
            self.destination.update()



    # ----------------- #
    # MOVEMENT / INPUTS #
    # ----------------- #
    
# Handles global and sessionwide inputs
    def inputs(self):
        window_inputs(self.window)
        ev = pg.event.get()
        for event in ev:
            if pg.mouse.get_pressed()[0]:
                self.move_player(self.player_f)
            if event.type == pg.QUIT:
                print("We wish to see you again!")
                sys.exit()
# Move the character towards the target on each tick
    def walk(self):
        if not self.destination_rect.colliderect(self.player_rect):
            self.player_f.x += self.p_speed * self.dx
            self.player_f.y += self.p_speed * self.dy

# Calculates the distance and direction on click
    def move_player(self, player: fe.Node):
        dest_x, dest_y = fe.get_mouse_pos(self)
        self.destination.x = dest_x
        self.destination.y = dest_y
        self.dx = dest_x - player.x
        self.dy = dest_y - player.y
        length = max(1, (self.dx ** 2 + self.dy ** 2) ** 0.5)
        self.dx /= length
        self.dy /= length
