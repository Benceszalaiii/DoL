import fusionengine as fe
import pygame as pg


class Destination:
    def __init__(self, win, x, y, width, height):
        self.destination: fe.Node = fe.Node(win, x, y, width, height)
        self.rect = pg.Rect(self.destination.x, self.destination.y, self.destination.width, self.destination.height)
    def load_rect(self, col: fe.Color):
        self.destination.load_rect(col)
    def update(self):
        self.rect.update(self.destination.x, self.destination.y, self.destination.width, self.destination.height)
        self.destination.update()