import os
import pygame as pg
from state import State
from utils import empty_terminal

print("Loading pause")
class PauseMenu(State):
    def __init__(self, game):
        self.game = game
        self.title = "DoL - Currently Playing (Paused)"
        State.__init__(self, game)
        pg.display.set_caption(self.title)
        self.resume = pg.rect.Rect(0, 0, 128, 72)
        self.resume.center = (self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT)
    def update(self, delta_time, actions):
        self.inputs(actions)

    def render(self, screen):
        pg.draw.rect(screen, "blue", self.resume)

    def inputs(self, actions):
        if actions["pause"]:
            actions["start"] = False
        if actions["resume"]:
            actions["start"] = True
            self.exit_state()
