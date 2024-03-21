import random
import pygame
import fusionengine as fe
from settings import WIDTH, HEIGHT, TITLE


class Projectile:
    def load_projectile(self):
        pass

    def run(self):
        pass

    def __init__(self, win: fe.Window):
        top_x: float = random.randint(0, WIDTH)
        top_y: float = 0
        top_x, top_y = random.randint(0, WIDTH), 0 if bool(random.randint(0, 1)) else 0, random.randint(0, WIDTH) if bool(random.randint(0, 1))  else random.randint(0, WIDTH), WIDTH if bool(random.randint(0, 1)) else WIDTH, random.randint(0, WIDTH) 
        top_proj: fe.Node = fe.Node(win, top_x, top_y, 50, 50)
