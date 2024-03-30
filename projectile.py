import random
import pygame
import math
import fusionengine as fe
from settings import SPEED, WIDTH, HEIGHT
from player import Player

proj_speed = 0


class Projectile:

    def __init__(self, win: fe.Window, dx: float, dy: float):
        self.dx = dx
        self.dy = dy
        self.window = win
        self.spawn()
        # self.all_bullets = []
        #                         Fentrol jon                                                            Balrol jon                                                     Lentrol jon                                                                                 Jobbrol jon
        # self.proj_x, self.proj_y = (random.randint(0, WIDTH), 0) if bool(random.randint(0, 1)) else (0, random.randint(0, HEIGHT)) if bool(random.randint(0, 1))  else (random.randint(0, WIDTH), HEIGHT - 50) if bool(random.randint(0, 1)) else (WIDTH - 50, random.randint(0, HEIGHT))
        

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

    def update(self):
        self.spawn_circumstance()
        self.proj.load_rect(fe.BLUE)
        self.distance_math()
        self.proj.x += self.speed_x
        self.proj.y += self.speed_y
        self.proj.update()

    def distance_math(self):
        distance_x = 10 - self.proj_x
        distance_y = 10 - self.proj_y
        angle = math.atan2(distance_y, distance_x)
        self.speed_x = 5 * math.cos(angle)
        self.speed_y = 5 * math.sin(angle)
        # self.all_bullets.append([self.proj_x, self.proj_y, self.speed_x, self.speed_y])

    def spawn(self):
            self._one_to_four()
            self.proj: fe.Node = fe.Node(self.window, self.proj_x, self.proj_y, 50, 50)

    def spawn_circumstance(self):
        #más lesz megadva végül
        if self.proj.x > WIDTH or self.proj.y > HEIGHT or self.proj.x < 0 or self.proj.y < 0:
            self.spawn()
            

    # def position(self):
    # self.mouse_pos: list[int] = []
    # for event in pygame.event.get():
    # if event.type == pygame.MOUSEBUTTONDOWN:
    # self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
    # self.mouse_pos.append(self.mouse_x)
    # self.mouse_pos.append(self.mouse_y)
    # return self.mouse_pos
    # return self.mouse_pos


# def list(self):
# for pos_x, pos_y, self.speed_x, self.speed_y in self.all_bullets:
# pos_x = int(pos_x)
# pos_y = int(pos_y)
