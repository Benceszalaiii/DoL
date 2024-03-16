import random
import pygame
import fusionengine as fusion
from settings import WIDTH, HEIGHT, TITLE, WINDOW


class Projectile:
    top_x: float = random.randint(0, WIDTH)
    top_y: float = 0
    top_proj: fusion.Node = fusion.Node(WINDOW, top_x, top_y, 50, 50)

    def projectile_top(self):
        pass

    def run(self):
        pass

    def __init__(self):
        pass
