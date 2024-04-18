from typing import Any
from config import Configuration
from state import State
from game import Game
import pygame as pg
from button import Button
from inputs import global_inputs, exit
from settings import SettingsMenu
from utils import clr
import os
from sound import Soundtrack

print("Loading menu")


class Menu(State):
    def __init__(self, game: Any, config: Any):
        State.__init__(self, game, config)
        self.title = "DoL - Main Menu"
        self.button_height = 100
        self.button_width = 400
        self.button_distance = 25
        self.soundtrack = Soundtrack(config.volume)
        self.soundtrack.start_menu()
        self.start = Button(
            x=self.game.GAME_WIDTH / 2 + 100,
            y=self.game.GAME_HEIGHT / 3 + 75,
            width=self.button_width,
            height=self.button_height,
            text="Start",
            font_size=36,
            font_color=(200, 200, 200),
            background_color=(204, 34, 41),
            hover_font_color=(200, 200, 200),
            hover_background_color=(145, 0, 0),
            cooler=True,
            cooler_color=(70, 55, 20),
        )
        self.settings_button = Button(
            x=self.game.screen_width / 2 + 100,
            y=self.start.rect.bottom + 2 * self.button_distance,
            width=self.button_width,
            height=self.button_height,
            text="Settings",
            font_size=20,
            font_color=(200, 200, 200),
            background_color=(3, 151, 171),
            hover_font_color=(200, 200, 200),
            hover_background_color=(9, 20, 40),
            cooler=True,
            cooler_color=(70, 55, 20),
        )
        self.quit_button = Button(
            x=self.game.screen_width / 2 + 100,
            y=self.settings_button.rect.bottom + self.button_distance,
            width=self.button_width,
            height=self.button_height,
            text="Exit",
            font_size=20,
            font_color=(200, 200, 200),
            background_color=(100, 100, 100),
            hover_font_color=(255, 255, 255),
            hover_background_color=(100, 0, 0),
        )
        self.logo = pg.image.load(os.path.join("assets", "logo.png")).convert_alpha()
        self.logo = pg.transform.scale(self.logo, (1000, 1000))
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.center = (200, self.game.screen_height / 2)
        self.actions = {"start": False, "click": False, "settings": False}
        self.background = pg.image.load(
            os.path.join("assets", "map", "background_blurred.png")
        )
        self.background = pg.transform.scale(
            self.background, (self.game.GAME_WIDTH, self.game.GAME_HEIGHT)
        )
        try:
            self.background = pg.transform.box_blur(self.background, 10)  # type: ignore
        except AttributeError:
            pass

    def update(self, delta_time: float, config: Configuration):
        if config.pause_quitted:
            self.soundtrack.start_menu()
            config.pause_quitted = False
        pg.display.set_caption(self.title)
        self.reset_keys()
        self.handle_events()
        if self.soundtrack.volume != config.volume:
            self.soundtrack.set_volume(config.volume)
        self.start.update(self.actions["click"])
        self.settings_button.update(self.actions["click"])
        self.quit_button.update(self.actions["click"])
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("Click")
        if self.actions["settings"]:
            new_state = SettingsMenu(self.game, self.config)
            new_state.enter_state()
        if self.actions["start"]:
            new_state = Game(self.game, self.config)
            self.reset_keys()
            new_state.enter_state()

    def render(self, screen: pg.surface.Surface):
        screen.fill((75, 0, 2))
        screen.blit(self.background, (0, 0))
        self.game.draw_text(
            screen,
            "Dodge of Legends",
            (200, 155, 60),
            self.game.GAME_WIDTH / 4 * 3 - 50,
            self.game.GAME_HEIGHT / 2 - 200,
            font_size=72,
        )
        screen.blit(self.logo, self.logo_rect)

        self.settings_button.render(screen)
        self.start.render(screen)
        self.quit_button.render(screen)

    def handle_events(self):
        for event in pg.event.get():
            global_inputs(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions["click"] = True
                    print("Click")
        if self.start.is_clicked:
            self.actions["start"] = True
            print("start")
        if self.settings_button.is_clicked:
            self.actions["settings"] = True
            print("settings")
        if self.quit_button.is_clicked:
            clr()
            print("We wish to see you again!")
            exit()
