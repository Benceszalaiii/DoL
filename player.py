# THIS IS THE FILE FOR THE PLAYER NODE


# --------- #
#  IMPORTS  #
# --------- #
import os
import pygame as pg
from settings import SPEED
from utils import empty_terminal
import math

# ------------------- #
#         NODE        #
# ------------------- #

class Player():

    # ------------------- #
    #   INITIALIZE NODE   #
    # ------------------- #

    def __init__(self, image_source: str, x: float, y: float, w: int, h: int):
        self.model = pg.image.load(image_source)
        self.rect = self.model.get_rect()
        self.model = pg.transform.scale(self.model, (w, h))
        self.crect = pg.rect.Rect((self.rect.centerx - 3), (self.rect.centery - 3), 6, 6)
        self.dest_cord = (self.crect.size)
        self.dest = pg.Rect(self.crect.x, self.crect.y, self.crect.width, self.crect.height)


    # ----------- #
    #   METHODS   #
    # ----------- #

# Updates elements of player

    def update(self, delta, actions, SW, SH):
        if actions["click"]:
            actions["click"] = False
            self.move_player(pg.mouse.get_pos())
        self.walk(delta)
        self.rect.update(self.crect.centerx - (self.crect.width/2), self.crect.centery - (self.crect.height/2), self.rect.width, self.rect.height)

    def render(self, screen: pg.surface):
        screen.blit(self.model, self.rect)
        pg.draw.rect(screen, "red", self.dest)
        pg.draw.rect(screen, "green", self.crect)
# Move the character towards the target on each tick
    def walk(self, delta):
        self.dx, self.dy = self.dest_cord[0] - self.crect.centerx, self.dest_cord[1] - self.crect.centery
        
        # Calculate the distance to the target position
        distance = math.hypot(self.dx, self.dy)
        if distance <= SPEED:
            self.crect.center = self.dest_cord
        self.dest.center = (self.dest_cord[0], self.dest_cord[1])
        # Scale the vector to the desired speed
        self.dx /= distance
        self.dy /= distance
        self.dx *= SPEED * delta
        self.dy *= SPEED * delta
        self.crect.centerx -= self.dx
        self.crect.centery -= self.dy


# Called on click, defines destination
    def move_player(self, target_pos):
        self.dest_cord = target_pos
        print(target_pos)