# THIS IS THE FILE FOR THE PLAYER NODE


# --------- #
#  IMPORTS  #
# --------- #
import pygame as pg
from projectile import Projectile
from math import atan2, cos, sin, sqrt
from config import Configuration
import os

print("Loading player")
# ------------------- #
#         NODE        #
# ------------------- #


class Player:
    # ------------------- #
    #   INITIALIZE NODE   #
    # ------------------- #

    def __init__(
        self,
        image_source: str,
        x: float,
        y: float,
        w: int,
        h: int,
        speed: float,
        config: Configuration,
    ):
        self.load_images()
        self.model = pg.image.load(
            os.path.join("assets", "sprites", "down_1.png")
        ).convert_alpha()
        self.model = pg.transform.scale(self.model, (64, 64))
        self.rect = self.model.get_rect()
        self.crect = pg.rect.Rect(
            x,
            y,
            self.rect.width / 6,
            self.rect.height / 6,
        )
        self.load_cursor()
        self.dest_img = pg.image.load(
            os.path.join("assets", "sprites", "ground_arrow (2).png")
        ).convert_alpha()
        self.dest_img = pg.transform.scale(self.dest_img, (16, 16))
        self.dest_cord = self.crect.size
        self.dest: pg.Rect = self.dest_img.get_rect()
        self.pos_x = x
        self.pos_y = y
        self.speed_x = 0
        self.speed_y = 0
        self.flash_icon = pg.image.load(os.path.join("assets", "flash.jpg"))
        self.flash_icon = pg.transform.scale(self.flash_icon, (35, 35))
        self.flash_pos = (config.width / 2 - 35, 0)
        self.ghost_icon = pg.image.load(os.path.join("assets", "ghost.png"))
        self.ghost_icon = pg.transform.scale(self.ghost_icon, (35, 35))
        self.ghost_pos = (config.width / 2, 0)
        self.hp = 100
        self.projectile = Projectile(config)
        self.dash_timer = 0
        self.dash_radius = 250
        self.speed = speed
        self.ghost_cooldown = 0
        self.ghost_timer = 0
        self.ghosted = False
        self.ghost_multiplier = 2
        self.ghost_multiplier_current = 1
        self.ui_rect = pg.Rect((config.width / 2 - 200, 0), (400, 35 + 10 + 15))
        self.hp_bar = pg.Rect((config.width / 2 - 200, 45), (400, 15))
        self.max_hp = 100
        self.direction = "down"
        self.prev_direction = "down"
        self.animation_frame = 0
        self.animation_delay = 50
        self.animation_time = 0
        self.cursor_frame = 9
        self.cursor_recently_pressed = False
        self.cursor_delay = 10
        self.cursor_animation_timer = 0
        self.spawn_rate = 1

    # ----------- #
    #   METHODS   #
    # ----------- #

    # Updates elements of player

    def update(self, delta: float, actions: dict[str, bool], config: Configuration):
        self.spawn_rate = min(3, self.spawn_rate + 0.001)
        if self.dash_timer >= 0:
            self.dash_timer -= delta / 250
        if self.ghosted:
            self.ghost_timer -= delta / 250
            if self.ghost_timer <= 0:
                self.ghosted = False
                self.ghost_multiplier_current = 1
        else:
            self.ghost_cooldown -= delta / 250
            if actions["ghost"]:
                self.ghost(config)
        if actions["click"]:
            self.move_player(pg.mouse.get_pos())
        # Move the character towards the target on each tick
        if actions["dash"]:
            self.dash(delta, pg.mouse.get_pos())
        if self.cursor_recently_pressed:
            self.cursor_animation_timer += 1
            if self.cursor_animation_timer % self.cursor_delay == 0:
                self.animate_click()
        else:
            self.cursor_animation_timer = 0
        self.walk(delta)

        self.crect.center = (self.pos_x, self.pos_y)  # type: ignore
        # Update the character's rect to match the updated position
        self.rect.update(
            self.crect.centerx - (self.rect.width / 2),
            self.crect.centery - (self.rect.height / 2),
            self.rect.width,
            self.rect.height,
        )
        self.projectile.update(delta, self.spawn_rate)
        self.projectile.collision(self.rect, self.crect)
        self.hp -= self.projectile.current_damage
        self.hp_bar.update(
            self.hp_bar.x, self.hp_bar.y, 400 * self.hp / self.max_hp, 15
        )
        self.hp_bar.centerx = config.width / 2
        if self.hp <= 0:
            actions["death"] = True
        self.prev_direction = self.direction
        self.direction = self.get_dominant_direction()
        self.animation_time += 1
        self.animate()

    def get_dominant_direction(self):
        # Check if stationary
        print(self.direction)
        if self.dest_cord == (int(self.pos_x), int(self.pos_y)):
            return "stationary"

        # Determine dominant direction based on absolute speed
        abs_speed_x = abs(self.speed_x)
        abs_speed_y = abs(self.speed_y)

        if abs_speed_x > abs_speed_y:
            return "right" if self.speed_x > 0 else "left"
        else:
            return "down" if self.speed_y > 0 else "up"

    def render(self, screen: pg.Surface):
        self.projectile.render(screen)
        screen.blit(self.model, self.rect)
        pg.draw.rect(screen, (1, 10, 19), self.ui_rect)
        pg.draw.rect(screen, "red", self.hp_bar)
        screen.blit(self.flash_icon, self.flash_pos)
        screen.blit(self.ghost_icon, self.ghost_pos)
        if self.cursor_recently_pressed:
            screen.blit(self.dest_img, self.dest)

    def move_player(self, target_pos: tuple[int, int]) -> None:
        """
        Calculates the distance and deltas needed to move each frame.
        :param target_pos: The position of the mouse.
        :return: None
        """
        mouse_x, mouse_y = target_pos
        self.dest.center = (mouse_x, mouse_y)
        self.cursor_recently_pressed = True
        distance_x = mouse_x - self.pos_x
        distance_y = mouse_y - self.pos_y
        angle = atan2(distance_y, distance_x)
        self.speed_x = self.speed * cos(angle)
        self.speed_y = self.speed * sin(angle)

    def walk(self, delta: float):
        if not self.dest.colliderect(self.crect):
            self.pos_x += self.speed_x * delta * self.ghost_multiplier_current
            self.pos_y += self.speed_y * delta * self.ghost_multiplier_current
        self.projectile.destination_logic(
            self.pos_x, self.pos_y, self.speed_x, self.speed_y, delta
        )

    def dash(self, delta: float, mouse_pos: tuple[int, int]) -> None:
        if self.dash_timer <= 0:
            self.speed_x, self.speed_y = 0, 0
            distance = self.dash_range(mouse_pos)
            if distance <= self.dash_radius:
                self.pos_x, self.pos_y = mouse_pos
            else:
                self.pos_x, self.pos_y = self.closest_point_on_radius(
                    mouse_pos, self.dash_radius
                )
            self.dash_timer = 15

    def ghost(self, config: Configuration):
        if self.ghost_cooldown <= 0:
            self.ghost_cooldown = 15
            self.ghosted = True
            self.ghost_multiplier_current = self.ghost_multiplier
            self.ghost_timer = 10

    def dash_range(self, point: tuple[int, int]) -> float:
        point_x, point_y = point
        center_x, center_y = self.crect.center

        # Calculate distance
        return sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)

    def closest_point_on_radius(self, point: tuple[int, int], radius: int):
        point_x, point_y = point
        circle_center_x, circle_center_y = self.crect.center

        # Direction vector
        dx = point_x - circle_center_x
        dy = point_y - circle_center_y

        # Normalize direction vector
        magnitude = sqrt(dx**2 + dy**2)
        if magnitude > 0:  # Avoid division by zero
            dx /= magnitude
            dy /= magnitude

        # Project onto circle with radius
        closest_x = circle_center_x + dx * radius
        closest_y = circle_center_y + dy * radius

        return (closest_x, closest_y)

    def animate(self):
        if (
            self.animation_time % self.animation_delay == 0
            or self.direction != self.prev_direction
        ):
            self.animation_frame += 1
            if self.prev_direction != self.direction:
                self.animation_frame = 0
            if self.direction == "stationary":
                self.animation_frame = 0
                self.model = self.down[0]
            else:
                if self.animation_frame >= len(self.down):
                    self.animation_frame = 0
                if self.direction == "right":
                    self.model = self.right[self.animation_frame]
                elif self.direction == "left":
                    self.model = self.left[self.animation_frame]
                elif self.direction == "up":
                    self.model = self.up[self.animation_frame]
                elif self.direction == "down":
                    self.model = self.down[self.animation_frame]

    def load_images(self):
        self.image_pointer = os.path.join("assets", "sprites")
        self.down: list[pg.Surface] = self.fill_direction("down")
        self.left: list[pg.Surface] = self.fill_direction("left")
        self.up: list[pg.Surface] = self.fill_direction("up")
        self.right: list[pg.Surface] = self.fill_direction("right")

    def fill_direction(self, direction: str) -> list[pg.Surface]:
        result = []
        for i in range(1, 4):
            name = self.image_pointer + "/" + direction + "_" + str(i) + ".png"
            print(name)
            result.append(self.load_image(name))
        return result

    def load_image(self, target: str):
        return pg.transform.scale(pg.image.load(target).convert_alpha(), (64, 64))

    def animate_click(self):
        if not self.cursor_frame >= len(self.cursor_frames) - 1:
            self.dest_img = self.cursor_frames[self.cursor_frame]
            self.cursor_frame += 1
        else:
            self.cursor_recently_pressed = False
            self.cursor_frame = 0

    def load_cursor(self):
        self.cursor_frames = []
        for i in range(2, 11):
            name = os.path.join(
                "assets", "sprites", "ground_arrow (" + str(i) + ").png"
            )
            self.cursor_frames.append(
                pg.transform.scale(pg.image.load(name).convert_alpha(), (16, 16))
            )
