import os

import pygame as pg

from state import State

from pause import PauseMenu
from player import Player

class Game(State):

    def __init__(self, game):

        State.__init__(self, game)

        self.background_img = pg.image.load(os.path.join(self.game.assets_dir, "map", "background.jpg"))
        self.background_img = pg.transform.scale(self.background_img, (self.game.GAME_WIDTH, self.game.GAME_HEIGHT))
        self.player = Player("player.jpg", self.background_img.get_rect().centerx, self.background_img.get_rect().centery, 200, 150)

    def update(self, delta_time, actions):

        # Check if the game was paused 

        if actions["start"]:

            new_state = PauseMenu(self.game)

            new_state.enter_state()

        self.player.update(delta_time, actions)

    def render(self, display):
        display.blit(self.background_img, (0,0))
        self.player.render(display)

    def inputs(self, actions):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.dx, self.dy = pg.mouse.get_pos()
