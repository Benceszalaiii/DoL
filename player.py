import fusionengine as fe
import pygame as pg
from destination import Destination
from settings import SPEED
class Player:
    def __init__(self, win, x, y, width, height):
        self.hitbox: fe.Node = fe.Node(win, win.width, win.height, 75, 175)
        self.crect = fe.Node(win, self.hitbox.x/2 - 5, self.hitbox.y/2 - 5, 10, 10)
        self.rect = pg.Rect(self.crect.x, self.crect.y, self.crect.width, self.crect.height)
        self.hitboxrect: pg.rect.Rect = pg.Rect(self.hitbox.x, self.hitbox.y, self.hitbox.width, self.hitbox.height)
        self.dx = 0
        self.dy = 0
    
    def load_rect(self, col: fe.Color):
        self.hitbox.load_rect(col)
# Updates elements of player        
    def update(self, dest: Destination):
        # Update calls
            self.hitbox.update()
            self.crect.update()
        # Movement
            self.walk(dest)
        # Pygame update calls
            self.rect.update(self.crect.x, self.crect.y, self.crect.width, self.crect.height)
            self.hitboxrect.update(self.hitbox.x, self.hitbox.y, self.hitbox.width, self.hitbox.height)
        # Syncronize hitbox with center rect (for movement)
            self.hitbox.x = self.crect.x - self.hitbox.width/2
            self.hitbox.y = self.crect.y - self.hitbox.height/2
    
    # Move the character towards the target on each tick
    def walk(self, dest: Destination):
        if not dest.rect.colliderect(self.rect):
            self.crect.x += SPEED * self.dx
            self.crect.y += SPEED * self.dy
