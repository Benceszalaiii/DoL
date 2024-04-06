import random
import pygame
import math
import pygame.math as pymath
from settings import SPEED, WIDTH, HEIGHT

# from player import Player

proj_speed = 0


class Projectile:

    def __init__(self, screen: pygame.Surface):
        # self.spawn()
        self.screen = screen
        self.lefutás_száma: int = 0
        self.all_bullets = []
        projectile = pygame.image.load("projpróba2.png")
        self.proj = pygame.transform.scale(projectile, [50, 30])

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
        # self.spawn_circumstance()
        self.lefutás_száma += 1
        if self.lefutás_száma % 500 == 0:
            self._one_to_four()
            self.distance_math()
        self.proj_movement()
        self.spawn()
        self.despawn()

    def distance_math(self):
        distance_x: float = WIDTH / 2 - self.proj_x
        distance_y: float = HEIGHT / 2 - self.proj_y
        self.angle: float = math.atan2(distance_y, distance_x)
        self.rotation_math()
        self.speed_x: float = 1 * math.cos(self.angle)
        self.speed_y: float = 1 * math.sin(self.angle)
        self.all_bullets.append(
            [self.proj_x, self.proj_y, self.speed_x, self.speed_y, self.rotation_vector]
        )

    def rotation_math(self):
        destination = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
        self_pos = pygame.Vector2(self.proj_x, self.proj_y)
        self.rotation_vector = destination - self_pos

    def proj_movement(self):
        for item in self.all_bullets:
            item[0] += item[2]
            item[1] += item[3]

    def spawn(self):
        for pos_x, pos_y, speed_x, speed_y, angle in self.all_bullets:
            # pygame.draw.rect(self.screen, (255, 0, 0), ((pos_x, pos_y), (30, 30)))
            degree = angle.as_polar()[1]
            print(degree)
            rotated_proj = pygame.transform.rotate(self.proj, -degree + 165)
            self.screen.blit(rotated_proj, ((pos_x, pos_y), (30, 30)))

    def despawn(self):
        for pos_x, pos_y, speed_x, speed_y, angle in self.all_bullets:
            if pos_x > WIDTH or pos_x < 0 or pos_y > HEIGHT or pos_y < 0:
                self.all_bullets.remove([pos_x, pos_y, speed_x, speed_y, angle])

