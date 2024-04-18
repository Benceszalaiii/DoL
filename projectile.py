import random
import pygame as pg
from math import atan2, cos, sin
from config import Configuration

proj_speed = 0
print("Loading projectile")

class Projectile:
    def __init__(self, config: Configuration):
        self.config = config
        self.delay_number: int = 0
        self.animation_frame: int = 0
        self.all_bullets = []
        self.destination_place: int = 1
        self.pictures_init()
        if not self.config.easter_egg:
            self.crop_pictures()
        else:
            self.cropped_animation = self.proj_animation
        self.resize_pictures()
        self.current_damage = 0
        self.cropped_animation = self.proj_animation

    def pictures_init(self):
        if not self.config.easter_egg:
            self.proj_animation: list[pg.Surface] = [
                pg.image.load("assets/sprites/projectile (1).png"),
                pg.image.load("assets/sprites/projectile (2).png"),
                pg.image.load("assets/sprites/projectile (3).png"),
                pg.image.load("assets/sprites/projectile (4).png"),
                pg.image.load("assets/sprites/projectile (5).png"),
                pg.image.load("assets/sprites/projectile (6).png"),
                pg.image.load("assets/sprites/projectile (7).png"),
                pg.image.load("assets/sprites/projectile (8).png"),
                pg.image.load("assets/sprites/projectile (9).png"),
                pg.image.load("assets/sprites/projectile (10).png"),
                pg.image.load("assets/sprites/projectile (11).png"),
            ]
        else:
            self.proj_animation: list[pg.Surface] = [
                pg.image.load("assets/sprites/easter_egg_1.jpg"),
                pg.image.load("assets/sprites/easter_egg_2.jpg"),
            ]

    def crop_pictures(self):
        self.cropped_animation: list[pg.Surface] = []
        for item in range(len(self.proj_animation)):
            cropped_item = self.proj_animation[item].subsurface(400, 200, 900, 600)
            self.cropped_animation.append(cropped_item)
        self.proj_animation = self.cropped_animation

    def resize_pictures(self):
        self.resized_animation: list[pg.Surface] = []

        for item in range(len(self.cropped_animation)):
            resized_item = pg.transform.scale(
                self.cropped_animation[item],
                [75, 45] if not self.config.easter_egg else [120, 90],
            )

            self.resized_animation.append(resized_item)
        self.proj_animation = self.resized_animation

    def _spawn_place(self):
        _side: int = random.randint(1, 4)
        if _side == 1:
            self.proj_x, self.proj_y = (random.randint(0, self.config.width), 0)
        elif _side == 2:
            self.proj_x, self.proj_y = (0, random.randint(0, self.config.height))
        elif _side == 3:
            self.proj_x, self.proj_y = (
                random.randint(0, self.config.width),
                self.config.height - 50,
            )
        else:
            self.proj_x, self.proj_y = (
                self.config.width - 50,
                random.randint(0, self.config.height),
            )

    def update(self, delta: float, spawnrate: float = 1):
        self.current_damage = 0
        self.delay_number += 1 if not self.config.easter_egg else 10
        calc = self.delay_number / spawnrate * 10 if self.config.easter_egg else self.delay_number * spawnrate
        if calc >= 250:
            self._spawn_place()
            self.destination_place: int = random.randint(1, 200)
            self.projectile_logic()
            self.delay_number = 0
        self.proj_movement(delta)

    def render(self, screen: pg.Surface):
        self.spawn(screen)
        self.despawn()

    def projectile_logic(self):
        distance_x: float = self.proj_dest_x - self.proj_x
        distance_y: float = self.proj_dest_y - self.proj_y
        angle: float = atan2(distance_y, distance_x)
        self.rotation_math()
        speed_x: float = 2 * cos(angle)
        speed_y: float = 2 * sin(angle)
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
        destination = pg.Vector2(self.proj_dest_x, self.proj_dest_y)
        self_pos = pg.Vector2(self.proj_x, self.proj_y)
        self.rotation_vector = destination - self_pos

    def proj_movement(self, delta: float):
        for item in self.all_bullets:
            item[0] += item[2] * delta
            item[1] += item[3] * delta

    def spawn(self, screen: pg.Surface):
        for pos_x, pos_y, speed_x, speed_y, angle in self.all_bullets:  #  type: ignore
            self.animation()
            degree: float = angle.as_polar()[1]
            rotated_proj: pg.Surface = pg.transform.rotate(
                self.resized_animation[self.animation_frame], -degree
            )
            if self.config.easter_egg:
                rotated_proj = self.resized_animation[self.animation_frame]
            screen.blit(rotated_proj, ((pos_x, pos_y), (75, 45)))

    def animation(self):
        if self.delay_number % 750 == 0:
            self.animation_frame += 1
            if self.animation_frame >= len(self.resized_animation):
                self.animation_frame = 0
        if not self.config.easter_egg and self.delay_number % 15 == 0:
            self.animation_frame += 1
            if self.animation_frame >= len(self.resized_animation):
                self.animation_frame = 0

    def despawn(self):
        for pos_x, pos_y, speed_x, speed_y, angle in self.all_bullets:
            if (
                pos_x > self.config.width + 75
                or pos_x < -75
                or pos_y > self.config.height + 75
                or pos_y < -75
            ):
                self.all_bullets.remove([pos_x, pos_y, speed_x, speed_y, angle])

    def destination_logic(
        self,
        pl_x: float,
        pl_y: float,
        pl_speed_x: float,
        pl_speed_y: float,
        delta: float,
    ):
        self.proj_dest_x: float = pl_x + pl_speed_x * delta * self.destination_place
        self.proj_dest_y: float = pl_y + pl_speed_y * delta * self.destination_place

    def collision(self, player: pg.Rect, center: pg.Rect):
        for pos_x, pos_y, speed_x, speed_y, angle in self.all_bullets:
            proj = pg.Rect(pos_x, pos_y, 75, 45)
            if proj.colliderect(player):
                self.current_damage += 10
                self.all_bullets.remove([pos_x, pos_y, speed_x, speed_y, angle])
