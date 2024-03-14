import random
import pygame
import fusionengine as fusion
from settings import WIDTH, HEIGHT


class Projectile():
    top_x: int = random.randint(0, WIDTH)
    top_y: int = 0

    def projectile_top(self):
        fusion.draw_rect(self.top_x, self.top_y, 50, 50, fusion.RED)
        pygame.Rect.move()



    def run(self):
        self.projectile_top()
        self.top_y += 5    

    def __init__(self):
        self.run()
