# THIS IS THE FILE FOR THE PLAYER NODE


# --------- #
#  IMPORTS  #
# --------- #
import os
import pygame as pg
from settings import SPEED


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
        self.rect.center = (x, y)
        self.crect = pg.rect.Rect((self.rect.centerx - 3), (self.rect.centery - 3), 6, 6)
        self.dx: float = 0
        self.dy: float = 0
        self.dest = pg.Rect(self.crect.x, self.crect.y, self.crect.width, self.crect.height)


    # ----------- #
    #   METHODS   #
    # ----------- #

# Updates elements of player

    def update(self, delta, actions):
        if actions["click"]:
            actions["click"] = False
            self.move_player()
        self.walk(delta)

    def render(self, screen: pg.surface):
        screen.blit(self.model, self.rect)
        pg.draw.rect(screen, "red", self.dest)
    # Move the character towards the target on each tick

    def walk(self, delta):
        if not self.crect.colliderect(self.dest):
            self.crect.x += SPEED * self.dx * delta
            self.crect.y += SPEED * self.dy * delta
    def move_player(self):

        dest_x, dest_y = pg.mouse.get_pos()
        self.dx = float(dest_x - self.crect.x)
        self.dy = float(dest_y - self.crect.y)
        print(dest_x," ", dest_y)
        self.dest.x = dest_x
        self.dest.y = dest_y
        length = max(1, (self.dx ** 2 + self.dy ** 2) ** 0.5)
        self.dx /= length
        self.dy /= length