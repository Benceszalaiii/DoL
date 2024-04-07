# THIS IS THE FILE FOR THE PLAYER NODE


# --------- #
#  IMPORTS  #
# --------- #
import pygame as pg
from settings import SPEED
from math import atan2, cos, sin
from projectile import Projectile
print("Loading player")
# ------------------- #
#         NODE        #
# ------------------- #


class Player:

    # ------------------- #
    #   INITIALIZE NODE   #
    # ------------------- #

    def __init__(self, image_source: str, x: float, y: float, w: int, h: int):
        self.model = pg.image.load(image_source)
        self.model = pg.transform.scale(self.model, (w, h))
        self.rect = self.model.get_rect()
        self.rect.topright = (x, y)
        self.crect = pg.rect.Rect(
            (self.rect.centerx - 3), (self.rect.centery - 3), self.rect.width/4, self.rect.height/4)
        self.dest_cord = (self.crect.size)
        self.dest = pg.Rect(self.crect.x, self.crect.y, 12, 12)
        self.movement = []
        self.pos_x = 0
        self.pos_y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.hp = 100
        self.regen_counter = 0
        self.projectile = Projectile()

    # ----------- #
    #   METHODS   #
    # ----------- #

# Updates elements of player

    def update(self, delta: float, actions: dict[str, bool]):
        if actions["click"]:
            self.move_player(pg.mouse.get_pos())
        # Move the character towards the target on each tick
        self.walk(delta)
        self.crect.center = (self.pos_x, self.pos_y)
        # Update the character's rect to match the updated position
        self.rect.update(self.crect.centerx - (self.rect.width/2), self.crect.centery -
                         (self.rect.height/2), self.rect.width, self.rect.height)
        self.projectile.update(delta)

    def render(self, screen: pg.Surface):
        screen.blit(self.model, self.rect)
        pg.draw.rect(screen, "red", self.crect)
        pg.draw.rect(screen, "green", self.dest)
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
        self.speed_x = SPEED * cos(angle)
        self.speed_y = SPEED * sin(angle)
        # self.movement.append([self.pos_x, self.pos_y, self.speed_x, self.speed_y])

    def walk(self, delta: float):
        if not self.dest.colliderect(self.crect):
            self.pos_x += self.speed_x * delta  # pos_x += speed_x
            self.pos_y += self.speed_y * delta
        self.projectile.destination_logic(self.pos_x, self.pos_y, self.speed_x, self.speed_y, delta)
