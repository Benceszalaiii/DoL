# THIS IS THE FILE FOR THE PLAYER NODE


# --------- #
#  IMPORTS  #
# --------- #
import os
import pygame as pg
from settings import SPEED
import math
print("Loading player")
# ------------------- #
#         NODE        #
# ------------------- #

class Player():

    # ------------------- #
    #   INITIALIZE NODE   #
    # ------------------- #

    def __init__(self, image_source: str, x: float, y: float, w: int, h: int):
        self.model = pg.image.load(image_source)
        self.model = pg.transform.scale(self.model, (w, h))
        self.rect = self.model.get_rect()
        self.rect.topright = (1400, 800)
        self.crect = pg.rect.Rect((self.rect.centerx - 3), (self.rect.centery - 3), 6, 6)
        self.dest_cord = (self.crect.size)
        self.dest = pg.Rect(self.crect.x, self.crect.y, self.crect.width, self.crect.height)
        self.dx, self.dy = 0, 0

    # ----------- #
    #   METHODS   #
    # ----------- #

# Updates elements of player

    def update(self, delta, actions):
        if actions["click"]:
            actions["click"] = False
            self.move_player(pg.mouse.get_pos())
        self.dest.center = self.dest_cord
        # Move the character towards the target on each tick
        self.walk(delta)

        # Update the character's rect to match the updated position
        self.rect.update(self.crect.centerx - (self.crect.width/2), self.crect.centery - (self.crect.height/2), self.rect.width, self.rect.height)

    def render(self, screen: pg.Surface):
        screen.blit(self.model, self.rect)
        pg.draw.rect(screen, "blue", self.rect)
        pg.draw.rect(screen, "red", self.dest)
        pg.draw.rect(screen, "green", self.crect)
    """    def walk(self, delta) -> None:
        
    Calculates the distance to the target position and updates the character's position.
    
    Args:
        delta (int): Time since last update in milliseconds.

    Returns:
        None

        
        if not self.crect.colliderect(self.dest):
        # Calculate the distance to the target position
            self.dx, self.dy = self.dest_cord[0] - self.crect.centery, self.dest_cord[1] - self.crect.centery
            self.dx = self.dx * SPEED * delta
            self.dy = self.dy * SPEED * delta
            self.crect.center = (self.crect.centerx + self.dx, self.crect.centery + self.dy)
            self.dest.center = (self.crect.centerx, self.crect.centery)
        else:
            print("Collided")"""
    def move_player(self, target_pos):
        # Set the target position to move towards
        self.dest_cord = target_pos
        dest_x, dest_y =  self.dest_cord
        self.dest.center = (dest_x, dest_y)
        self.dx = float(dest_x - self.crect.x)
        self.dy = float(dest_y - self.crect.y)
        length = max(1, (self.dx ** 2 + self.dy ** 2) ** 0.5)
        print(self.dx, self.dy)
        self.dx /= length
        self.dy /= length
    def walk(self, delta):
        if not self.crect.colliderect(self.dest):
            self.crect.centerx += SPEED * self.dx * delta
            self.crect.centery += SPEED * self.dy * delta
        else:
            print("Collided")