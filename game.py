import pygame
import sys
import random
from pygame.locals import *
from settings import FPS, BG_COLOR, WIDTH, HEIGHT, TITLE
import fusionengine as fusion


class Game(object):
    window: fusion.Window
    def window_inputs(self):
        if fusion.key_down_once(fusion.KEY_F1):
            self.window.toggle_fullscreen()


    def __init__(self):
        self.window = fusion.Window(TITLE, HEIGHT, WIDTH)
        self.window.set_fps(FPS)
        self.window.change_icon(fusion.DEBUGIMAGE)

        @self.window.loop
        def loop():
            fusion.draw_image(fusion.DEBUGIMAGE, 0, 0, WIDTH/2, HEIGHT/2)
            self.window_inputs()