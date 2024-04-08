# THIS IS THE FILE FOR THE PLAYER NODE


# --------- #
#  IMPORTS  #
# --------- #
import pygame as pg
from projectile import Projectile
from math import atan2, cos, sin, sqrt

print("Loading player")
# ------------------- #
#         NODE        #
# ------------------- #


class Player:
    # ------------------- #
    #   INITIALIZE NODE   #
    # ------------------- #

    def __init__(self, image_source: str, x: float, y: float, w: int, h: int, speed: float):
        self.model = pg.image.load(image_source)
        self.model = pg.transform.scale(self.model, (w, h))
        self.rect = self.model.get_rect()
        self.crect = pg.rect.Rect(
            x,
            y,
            self.rect.width / 6,
            self.rect.height / 6,
        )
        self.dest_cord = self.crect.size
        self.dest = pg.Rect(self.crect.x, self.crect.y, 12, 12)
        self.pos_x = x
        self.pos_y = y
        self.speed_x = 0
        self.speed_y = 0
        self.hp = 100
        self.regen_counter = 0
        self.projectile = Projectile()
        self.dash_timer = 0
        self.dash_radius = 250
        self.speed = speed


    # ----------- #
    #   METHODS   #
    # ----------- #

    # Updates elements of player

    def update(self, delta: float, actions: dict[str, bool]):
        if self.dash_timer >= 0:
            self.dash_timer -= delta

        if actions["click"]:
            self.move_player(pg.mouse.get_pos())
        # Move the character towards the target on each tick
        if actions["dash"]:
            self.dash(delta, pg.mouse.get_pos())
        
        self.walk(delta)
        self.crect.center = (self.pos_x, self.pos_y)
        # Update the character's rect to match the updated position
        self.rect.update(
            self.crect.centerx - (self.rect.width / 2),
            self.crect.centery - (self.rect.height / 2),
            self.rect.width,
            self.rect.height,
        )
        self.projectile.update(delta)
        self.projectile.collision(self.rect, self.crect)

    def render(self, screen: pg.Surface):
        screen.blit(self.model, self.rect)
        self.projectile.render(screen)

    def move_player(self, target_pos: tuple[int, int]) -> None:
        """
        Calculates the distance and deltas needed to move each frame.
        :param target_pos: The position of the mouse.
        :return: None
        """
        mouse_x, mouse_y = target_pos
        self.dest.center = (mouse_x, mouse_y)
        distance_x = mouse_x - self.pos_x
        distance_y = mouse_y - self.pos_y
        angle = atan2(distance_y, distance_x)
        self.speed_x = self.speed * cos(angle)
        self.speed_y = self.speed * sin(angle)

    def walk(self, delta: float):
        if not self.dest.colliderect(self.crect):
            self.pos_x += self.speed_x * delta  # pos_x += speed_x
            self.pos_y += self.speed_y * delta
        self.projectile.destination_logic(self.pos_x, self.pos_y, self.speed_x, self.speed_y, delta)

    def dash(self, delta: float, mouse_pos: tuple[int, int])-> None:
        if self.dash_timer <= 0:
            self.speed_x, self.speed_y = 0, 0
            distance = self.dash_range(mouse_pos)
            if distance <= self.dash_radius:
                self.pos_x, self.pos_y = mouse_pos
            else:
                self.pos_x, self.pos_y = self.closest_point_on_radius(mouse_pos, self.dash_radius)
            self.dash_timer = 5 * 250


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
        magnitude = sqrt(dx ** 2 + dy ** 2)
        if magnitude > 0:  # Avoid division by zero
            dx /= magnitude
            dy /= magnitude

        # Project onto circle with radius
        closest_x = circle_center_x + dx * radius
        closest_y = circle_center_y + dy * radius

        return (closest_x, closest_y)
