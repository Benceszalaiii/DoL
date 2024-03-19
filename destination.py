import fusionengine as fe
import pygame as pg


class Destination:
    def __init__(self, win, x, y, width, height):
        self.destination: fe.Node = fe.Node(win, x, y, 10, 10)
        self.rect = pg.Rect(self.destination.x, self.destination.y, self.destination.width, self.destination.height)