from operator import methodcaller
import random
import pygame
import math
import time
import pygame.math as pymath
from settings import SPEED, WIDTH, HEIGHT

# from player import Player

proj_speed = 0


class Projectile:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.lefutás_száma: int = 0
        self.animation_frame: int = 0
        # self.frame: int = 0
        self.all_bullets = []
        self.pictures_init()
        self.crop_pictures()
        self.resize_pictures()
        # self.starttime = time.time()
        # self.timer = Timer(3, self._spawn_place, self._spawn_place(), self.projectile_logic())

        # proj = pygame.image.load("projpróba2.png")
        # self.resized_proj = pygame.transform.scale(proj, [50, 30])

    def pictures_init(self):
        self.proj_animation = [
            pygame.image.load("assets/sprites/projectile (1).png"),
            pygame.image.load("assets/sprites/projectile (2).png"),
            pygame.image.load("assets/sprites/projectile (3).png"),
            pygame.image.load("assets/sprites/projectile (4).png"),
            pygame.image.load("assets/sprites/projectile (5).png"),
            pygame.image.load("assets/sprites/projectile (6).png"),
            pygame.image.load("assets/sprites/projectile (7).png"),
            pygame.image.load("assets/sprites/projectile (8).png"),
            pygame.image.load("assets/sprites/projectile (9).png"),
            pygame.image.load("assets/sprites/projectile (10).png"),
            pygame.image.load("assets/sprites/projectile (11).png"),
        ]

    def crop_pictures(self):
        self.cropped_animation = []
        for item in range(len(self.proj_animation)):
            cropped_item = self.proj_animation[item].subsurface(400, 200, 900, 600)
            self.cropped_animation.append(cropped_item)

    def resize_pictures(self):
        self.resized_animation = []
        for item in range(len(self.cropped_animation)):
            resized_item = pygame.transform.scale(
                self.cropped_animation[item], [75, 45]
            )
            self.resized_animation.append(resized_item)

    def _spawn_place(self):
        _side: int = random.randint(1, 4)
        if _side == 1:
            self.proj_x, self.proj_y = (random.randint(0, WIDTH), 0)
        elif _side == 2:
            self.proj_x, self.proj_y = (0, random.randint(0, HEIGHT))
        elif _side == 3:
            self.proj_x, self.proj_y = (random.randint(0, WIDTH), HEIGHT - 50)
        else:
            self.proj_x, self.proj_y = (WIDTH - 50, random.randint(0, HEIGHT))

    def update(self):
        # self.spawn_circumstance()
        # cur_time = time.time()
        # time_passed = cur_time - self.starttime
        self.lefutás_száma += 1
        if self.lefutás_száma % 500 == 0:
            self._spawn_place()
            self.projectile_logic()
        self.proj_movement()
        self.spawn()
        self.despawn()

    def projectile_logic(self):
        distance_x: float = WIDTH / 2 - self.proj_x
        distance_y: float = HEIGHT / 2 - self.proj_y
        angle: float = math.atan2(distance_y, distance_x)
        self.rotation_math()
        speed_x: float = 1 * math.cos(angle)
        speed_y: float = 1 * math.sin(angle)
        self.all_bullets.append(
            [
                self.proj_x,
                self.proj_y,
                speed_x,
                speed_y,
                self.rotation_vector,
            ]
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
            self.animation()
            degree = angle.as_polar()[1]
            rotated_proj = pygame.transform.rotate(
                self.resized_animation[self.animation_frame], -degree
            )
            self.screen.blit(rotated_proj, ((pos_x, pos_y), (100, 100)))

    def animation(self):
        if self.lefutás_száma % 30 == 0:
            self.animation_frame += 1
            if self.animation_frame >= len(self.resized_animation):
                self.animation_frame = 0

    def despawn(self):
        for pos_x, pos_y, speed_x, speed_y, angle in self.all_bullets:
            if pos_x > WIDTH or pos_x < 0 or pos_y > HEIGHT or pos_y < 0:
                self.all_bullets.remove([pos_x, pos_y, speed_x, speed_y, angle])
