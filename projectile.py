import random
import pygame
import math
import fusionengine as fe
from settings import SPEED, WIDTH, HEIGHT
from player import Player

proj_speed = 0


class Projectile:

    def __init__(self, win: fe.Window, dx: float, dy: float):
        # self.top_x: float = random.randint(0, WIDTH)
        # self.top_y: float = 0
        self.dx = dx
        self.dy = dy
        self._one_to_four()
        self.all_bullets: list[float] = []
        #                         Fentrol jon                                                            Balrol jon                                                     Lentrol jon                                                                                 Jobbrol jon
        # self.proj_x, self.proj_y = (random.randint(0, WIDTH), 0) if bool(random.randint(0, 1)) else (0, random.randint(0, HEIGHT)) if bool(random.randint(0, 1))  else (random.randint(0, WIDTH), HEIGHT - 50) if bool(random.randint(0, 1)) else (WIDTH - 50, random.randint(0, HEIGHT))
        self.top_proj: fe.Node = fe.Node(win, self.proj_x, self.proj_y, 50, 50)
        # self.top_proj: fe.Node = fe.Node(win, self.top_x, self.top_y, 50, 50)

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

    def proj_speed(self):
        player_x = SPEED * Player.dx * 3

    def update(self):
        self.top_proj.load_rect(fe.BLUE)
        # self._move()
        self.top_proj.update()

    def distance_math(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        distance_x = mouse_x - player.x
        distance_y = mouse_y - player.y
        angle = math.atan2(distance_y, distance_x)
        speed_x = SPEED * math.cos(angle)
        speed_y = SPEED * math.sin(angle)
        self.all_bullets.append([player.x, player.y, speed_x, speed_y])

    def position(self):
        for event in pygame.event.get():
            if event == pygame.MOUSEBUTTONDOWN:
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
