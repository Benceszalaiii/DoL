import fusionengine as fe
import pygame as pg
class Player:
    def __init__(self, win, x, y, width, height):
        self.hitbox: fe.Node = fe.Node(win, win.width, win.height, 75, 175)
        self.crect = fe.Node(win, self.hitbox.x/2 - 5, self.hitbox.y/2 - 5, 10, 10)
        self.rect = pg.Rect(self.crect.x, self.crect.y, self.crect.width, self.crect.height)
        