import pygame
import sys
import random
from pygame.locals import *
from settings import FPS, BG_COLOR, WIDTH, HEIGHT, TITLE


class Game(object):
    def __init__(self):
        pygame.init()
        clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.screen.fill(BG_COLOR)
        self._running = True
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.quit():
                    self._running = False
                    sys.exit()
            clock.tick(FPS)
