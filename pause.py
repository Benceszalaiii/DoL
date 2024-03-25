import os
import pygame as pg
from state import State

class PauseMenu(State):
    def __init__(self, game):
        self.game = game
        State.__init__(self, game)


    def update(self, delta_time, actions):  
        pass

    def render(self, display):
        pass