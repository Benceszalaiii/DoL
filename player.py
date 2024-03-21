# THIS IS THE FILE FOR THE PLAYER NODE


# --------- #
#  IMPORTS  #
# --------- #

import fusionengine as fe
import pygame as pg
from destination import Destination
from settings import SPEED


# ------------------- #
#         NODE        #
# ------------------- #

class Player:

    # ------------------- #
    #   INITIALIZE NODE   #
    # ------------------- #

    def __init__(self, win: fe.Window, x: float, y: float, w: int, h: int): 
        self.crect_init(win)
        self.hitbox_init(win, x, y, w, h)
        self.dest_init()

# Initialize the center rect (used for movement)
    def crect_init(self, win: fe.Window) -> None:
        self.crect = fe.Node(win, self.hitbox.x/2 - 5, self.hitbox.y/2 - 5, 10, 10)
        self.rect = pg.Rect(self.crect.x, self.crect.y, self.crect.width, self.crect.height)

# Initializes the hitbox (also the image holder)
    def hitbox_init(self, win: fe.Window, x: float, y: float, w: int, h: int) -> None: 
        self.hitbox: fe.Node = fe.Node(win, x, y, w, h)
        self.hitboxrect: pg.rect.Rect = pg.Rect(self.hitbox.x, self.hitbox.y, self.hitbox.width, self.hitbox.height)


    def dest_init(self) -> None:
        self.dx: float = 0
        self.dy: float = 0


    # ----------- #
    #   METHODS   #
    # ----------- #

# Handle coloring the hitbox

    def load_rect(self, col: fe.Color):
        self.hitbox.load_rect(col)

# Handle images on the hitbox

    def load_image(self, img: str):
        self.hitbox.load_image(img)

# Updates elements of player

    def update(self, dest: Destination):
        # Update calls
        self.hitbox.update()
        self.crect.update()
        # Movement
        self.walk(dest)
        # Pygame update calls
        self.rect.update(self.crect.x, self.crect.y, self.crect.width, self.crect.height)
        self.hitboxrect.update(self.hitbox.x, self.hitbox.y, self.hitbox.width, self.hitbox.height)
        # Syncronize hitbox with center rect (for movement)
        self.hitbox.x = self.crect.x - self.hitbox.width/2
        self.hitbox.y = self.crect.y - self.hitbox.height/2

    # Move the character towards the target on each tick

    def walk(self, dest: Destination):
        if not dest.rect.colliderect(self.rect):
            self.crect.x += SPEED * self.dx
            self.crect.y += SPEED * self.dy
