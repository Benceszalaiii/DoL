# THIS IS THE FILE FOR THE PLAYER NODE


# --------- #
#  IMPORTS  #
# --------- #
import os
import pygame as pg
from settings import SPEED
from math import atan2, cos, sin
from utils import empty_terminal as clr
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
        self.rect.topright = (x, y)
        self.crect = pg.rect.Rect((self.rect.centerx - 3), (self.rect.centery - 3), self.rect.width/4, self.rect.height/4)
        self.dest_cord = (self.crect.size)
        self.dest = pg.Rect(self.crect.x, self.crect.y, 12, 12)
        
        self.movement = []
        self.pos_x = 0
        self.pos_y = 0
        self.speed_x = 0
        self.speed_y = 0
        
    # ----------- #
    #   METHODS   #
    # ----------- #

# Updates elements of player

    def update(self, delta, actions):
        if actions["click"]:
            actions["click"] = False
            self.move_player(pg.mouse.get_pos())
        # Move the character towards the target on each tick
        self.walk(delta)
                # Update the character's rect to match the updated position
        self.rect.update(self.crect.centerx - (self.rect.width/2), self.crect.centery - (self.rect.height/2), self.rect.width, self.rect.height)
        

    def render(self, screen: pg.Surface):
        screen.blit(self.model, self.rect)
        pg.draw.rect(screen, "red", self.dest)
        pg.draw.rect(screen, (255, 0, 0), ((self.pos_x, self.pos_y), (30, 30)))

        """
        pg.draw.rect(screen, "green", self.crect)"""
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
        mouse_x, mouse_y = target_pos
        distance_x = mouse_x - self.pos_x
        distance_y = mouse_y - self.pos_y
        angle = atan2(distance_y, distance_x)
        self.speed_x = SPEED * cos(angle)
        self.speed_y = SPEED * sin(angle)
        #self.movement.append([self.pos_x, self.pos_y, self.speed_x, self.speed_y])


    def walk(self, delta: float):
        self.pos_x += self.speed_x * delta  # pos_x += speed_x
        self.pos_y += self.speed_y * delta

