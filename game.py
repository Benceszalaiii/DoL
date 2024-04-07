from inputs import global_inputs
import os

import pygame as pg

from config import CLICK, FLASH
from state import State
from pause import PauseMenu
from player import Player

print("Loading game")
if CLICK == "right":  # type: ignore STUPID PYLANCE
    click_preference = 3
elif CLICK == "left":
    click_preference = 1
else:
    raise ValueError("Unknown click preference, click must either be 'right' or 'left")

if FLASH == "D":
    flash_preference = pg.K_d
elif FLASH == "F":
    flash_preference = pg.K_f
else:
    raise ValueError("The imported value for FLASH must be either D or F")

class Game(State):
    def __init__(self, game):  # type: ignore
        self.title = "DoL - Currently Playing"
        pg.display.set_caption(self.title)
        State.__init__(self, game)
        self.game = game
        self.load_dir_ptrs()
        self.background_img = pg.image.load(
            os.path.join(self.map_dir, "background.jpg")
        )
        self.background_img = pg.transform.scale(
            self.background_img, (self.game.GAME_WIDTH, self.game.GAME_HEIGHT)
        )
        self.player = Player(
            os.path.join(self.sprite_dir, "player.jpg"),
            self.game.screen_width /2,
            self.game.screen_height /2,
            90,
            140,
        )
        self.actions = {"pause": False, "quit": False, "click": False, "dash": False}
        self.dash_rect_thickness = 20
        self.dash_rect_full = pg.Rect(30, 30, 200, self.dash_rect_thickness)
        self.dash_rect_active = pg.Rect(30, 30, 0, self.dash_rect_thickness)
        
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
        self.dash_rect_active.update(30, 30, min(200, self.player.dash_timer), self.dash_rect_thickness)   #  /5 * 200 (Because 5 second is the cooldown and 200px is max width)
        self.reset_keys()

    def render(self, screen: pg.Surface):
        screen.blit(self.background_img, (0, 0))
        self.player.render(screen)
        pg.draw.rect(screen, "black", self.dash_rect_full)
        pg.draw.rect(screen, "yellow", self.dash_rect_active)

    def handle_events(self):
        for event in pg.event.get():
            global_inputs(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.actions["pause"] = True
                if event.key == pg.K_BACKSPACE:
                    self.actions["quit"] = True
                if event.key == flash_preference:
                    self.actions["dash"] = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == click_preference:
                    self.actions["click"] = True
