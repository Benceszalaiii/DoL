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
        self.dest.center = self.dest_cord
        # Move the character towards the target on each tick
        self.walk(delta)

        # Update the character's rect to match the updated position
        self.rect.update(self.crect.centerx - (self.crect.width/2), self.crect.centery - (self.crect.height/2), self.rect.width, self.rect.height)

    def render(self, screen: pg.Surface):
        pg.draw.rect(screen, "blue", self.rect)
        screen.blit(self.model, self.rect)
        pg.draw.rect(screen, "red", self.dest)
        pg.draw.rect(screen, "green", self.crect)
    def walk(self, delta):
        # Calculate the distance to the target position
        self.dx, self.dy = self.dest_cord[0] - self.crect.centery, self.dest_cord[1] - self.crect.centery
        distance = math.hypot(self.dx, self.dy)

        # Check if the character has reached the destination
        if distance <= SPEED * delta:
            self.crect.center = self.dest_cord
        else:
            # Calculate the movement increment based on delta time
            direction_x, direction_y = self.dx / distance, self.dy / distance
            move_x = direction_x * SPEED * delta
            move_y = direction_y * SPEED * delta
            print(f"Distance: {distance}, Move X: {move_x}, Move Y: {move_y}")
            # Update the character's position
            self.crect.centerx += move_x
            self.crect.centery += move_y
    def move_player(self, target_pos):
        # Set the target position to move towards
        self.dest_cord = target_pos
