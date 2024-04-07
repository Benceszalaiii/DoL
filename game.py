from inputs import global_inputs
import os

import pygame as pg

from settings import CLICK
from state import State
from pause import PauseMenu  # type: ignore
from player import Player
from projectile import Projectile
print("Loading game")
CLICK_PREFERENCE = 3 if CLICK == "right" else 1


class Game(State):

    def __init__(self, game):  # type: ignore
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
        ).centerx, self.background_img.get_rect().centery, 100, 150)
        self.actions = {"pause": False, "quit": False, "click": False}
        self.projectile = Projectile()

    def load_dir_ptrs(self):
        self.sprite_dir = os.path.join(self.game.assets_dir, "sprites")
        self.map_dir = os.path.join(self.game.assets_dir, "map")

    def update(self, delta_time: float):
        self.handle_events()
        # Check if the game was paused
        if self.actions["quit"]:
            self.reset_keys()
            self.exit_state()
        if self.actions["pause"]:
            new_state = PauseMenu(self.game)
            new_state.enter_state()

        self.player.update(delta_time, self.actions)
        self.projectile.update(delta_time)
        self.reset_keys()

        


    def render(self, screen: pg.Surface):
        screen.blit(self.background_img, (0, 0))
        self.player.render(screen)
        self.projectile.render(screen)

    def handle_events(self):
        for event in pg.event.get():
            global_inputs(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.actions["pause"] = True
                if event.key == pg.K_BACKSPACE:
                    self.actions["quit"] = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == CLICK_PREFERENCE:
                    self.actions["click"] = True
