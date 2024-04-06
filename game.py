import os

import pygame as pg

from state import State

from pause import PauseMenu
from player import Player
print("Loading game")


class Game(State):

    def __init__(self, game):
        self.title = "DoL - Currently Playing"
        pg.display.set_caption(self.title)
        State.__init__(self, game)
        self.game = game
        self.load_dir_ptrs()
        self.background_img = pg.image.load(
            os.path.join(self.map_dir, "background.jpg"))
        self.background_img = pg.transform.scale(
            self.background_img, (self.game.GAME_WIDTH, self.game.GAME_HEIGHT))
        self.player = Player(os.path.join(self.sprite_dir, "player.jpg"), self.background_img.get_rect(
        ).centerx, self.background_img.get_rect().centery, 200, 150)

    def load_dir_ptrs(self):
        self.sprite_dir = os.path.join(self.game.assets_dir, "sprites")
        self.map_dir = os.path.join(self.game.assets_dir, "map")

    def update(self, delta_time, actions):
        # Check if the game was paused
        if actions["pause"]:
            self.exit_state()
            """ new_state = PauseMenu(self.game)

            new_state.enter_state()"""

        self.player.update(delta_time, actions)

    def render(self, screen: pg.Surface):
        screen.blit(self.background_img, (0, 0))
        self.player.render(screen)
