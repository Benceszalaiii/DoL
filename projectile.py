import random
import pygame
import fusionengine as fe
from settings import WIDTH, HEIGHT

proj_speed = 8
class Projectile():

    def __init__(self, win: fe.Window, dx: float, dy: float):
        #self.top_x: float = random.randint(0, WIDTH)
        #self.top_y: float = 0
        self.dx = dx
        self.dy = dy
        self._one_to_four()
        #                         Fentrol jon                                                            Balrol jon                                                     Lentrol jon                                                                                 Jobbrol jon
        #self.proj_x, self.proj_y = (random.randint(0, WIDTH), 0) if bool(random.randint(0, 1)) else (0, random.randint(0, HEIGHT)) if bool(random.randint(0, 1))  else (random.randint(0, WIDTH), HEIGHT - 50) if bool(random.randint(0, 1)) else (WIDTH - 50, random.randint(0, HEIGHT))
        self.top_proj: fe.Node = fe.Node(win, self.proj_x, self.proj_y, 50, 50)
        #self.top_proj: fe.Node = fe.Node(win, self.top_x, self.top_y, 50, 50)

    def _one_to_four(self):
        _chance: int = random.randint(1, 4)
        if _chance == 1:
            self.proj_x, self.proj_y = (random.randint(0, WIDTH), 0)
        elif _chance == 2:
            self.proj_x, self.proj_y = (0, random.randint(0, HEIGHT))
        elif _chance == 3:
            self.proj_x, self.proj_y = (random.randint(0, WIDTH), HEIGHT - 50)
        else:
            self.proj_x, self.proj_y = (WIDTH - 50, random.randint(0, HEIGHT))

    #def _move(self):
        #self.top_proj.x += proj_speed * self.dx
        #self.top_proj.y += proj_speed * self.dy

    def update(self):
        self.top_proj.load_rect(fe.BLUE)
        #self._move()
        self.top_proj.update()
