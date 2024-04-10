from inputs import global_inputs
import os

import pygame as pg
from sound import Soundtrack
from state import State
from pause import PauseMenu
from player import Player
from deathscreen import Deathscreen
import time


class Game(State):
    def __init__(self, game, config):  # type: ignore
        self.title = "DoL - Currently Playing"
        State.__init__(self, game, config)
        self.game = game
        self.start_time = time.time()
        self.load_dir_ptrs()
        self.background_img = pg.image.load(
            os.path.join(self.map_dir, "background.jpg")
        )
        self.background_img = pg.transform.scale(
            self.background_img, (self.game.GAME_WIDTH, self.game.GAME_HEIGHT)
        )
        self.player = Player(
            os.path.join(self.sprite_dir, "player.jpg"),
            self.game.screen_width / 2,
            self.game.screen_height / 2,
            90,
            140,
            self.config.speed,
            self.config,
        )
        self.actions = {
            "pause": False,
            "quit": False,
            "click": False,
            "dash": False,
            "ghost": False,
            "death": False,
        }
        self.dash_rect_thickness = 10
        self.dash_rect_max_width = 200
        self.dash_rect_active = pg.Rect(0, 35, 0, self.dash_rect_thickness)
        self.dash_rect_active.right = config.width / 2
        self.ghost_rect_active = pg.Rect(0, 35, 0, self.dash_rect_thickness)
        self.ghost_rect_active.left = config.width / 2
        self.spawn_rate = 1
        self.soundtrack = Soundtrack(self.config.volume)
        self.soundtrack.start_game()

    def load_dir_ptrs(self):
        self.sprite_dir = os.path.join(self.game.assets_dir, "sprites")
        self.map_dir = os.path.join(self.game.assets_dir, "map")

    def update(self, delta_time: float, config):  # type: ignore
        pg.display.set_caption(self.title)
        self.handle_events()
        # Check if the game was paused
        self.player.update(delta_time, self.actions, self.config)
        current_dash_width = min(
            self.dash_rect_max_width,
            self.dash_rect_max_width
            - self.dash_rect_max_width / 15 * self.player.dash_timer,
        )
        self.dash_rect_active.update(
            self.ghost_rect_active.x - current_dash_width,
            self.dash_rect_active.y,
            current_dash_width,
            self.dash_rect_thickness,
        )
        self.ghost_rect_active.update(
            self.ghost_rect_active.x,
            self.ghost_rect_active.y,
            min(
                self.dash_rect_max_width,
                self.dash_rect_max_width
                - self.dash_rect_max_width / 15 * self.player.ghost_cooldown,
            ),
            self.dash_rect_thickness,
        )
        #  /5 * 200 (Because 5 second is the cooldown and 200px is max width)
        if self.actions["death"]:
            new_state = Deathscreen(self.game, self.config)
            new_state.enter_state()
        if self.actions["quit"]:
            self.reset_keys()
            self.soundtrack.start_menu()
            self.exit_state()
        if self.actions["pause"]:
            new_state = PauseMenu(self.game, self.config)
            new_state.enter_state()
        self.reset_keys()

    def render(self, screen: pg.Surface):
        screen.blit(self.background_img, (0, 0))
        self.player.render(screen)
        pg.draw.rect(screen, "yellow", self.dash_rect_active)
        pg.draw.rect(screen, "lightblue", self.ghost_rect_active)

    def handle_events(self):
        for event in pg.event.get():
            global_inputs(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.actions["pause"] = True
                if event.key == self.config.FLASH_KEY:
                    self.actions["dash"] = True
                if event.key == self.config.GHOST_KEY:
                    self.actions["ghost"] = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == self.config.CLICK_KEY:
                    self.actions["click"] = True
