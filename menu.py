from turtle import width
from typing import Any
from state import State
from game import Game
import pygame as pg
from button import Button
from inputs import global_inputs, exit
from settings import SettingsMenu
from utils import clr
print("Loading menu")


class Menu(State):
    def __init__(self, game: Any, config: Any):
        State.__init__(self, game, config)
        self.title = "DoL - Main Menu"
        pg.display.set_caption(self.title)
        self.button_height = 100
        self.start = Button(
            x=self.game.GAME_WIDTH / 2 - 100,
            y=self.game.GAME_HEIGHT / 2 ,
            width=200,
            height=self.button_height,
            text="Start",
            font_size=36,
            font_color=(200, 200, 200),
            background_color=(100, 100, 100),
            hover_font_color=(200, 200, 200),
            hover_background_color=(0, 100, 0),
        )
        self.settings_button = Button(
            x=self.game.screen_width / 2 - 100,
            y=self.game.screen_height / 2 + 100,
            width=200,
            height=self.button_height,
            text="Settings",
            font_size=20,
            font_color=(200, 200, 200),
            background_color=(100, 100, 100),
            hover_font_color=(200, 200, 200),
            hover_background_color=(100, 0, 0),
        )
        self.quit_button = Button(
            x=self.game.screen_width /2 - 100,
            y=self.game.screen_height -160,
            width=200,
            height=100,
            text="Exit",
            font_size=20,
            font_color=(200, 200, 200),
            background_color=(100, 100, 100),
            hover_font_color=(255, 255, 255),
            hover_background_color=(255, 0, 0),
        )
        self.actions = {"start": False, "click": False, "settings": False}

    def update(self, delta_time: float):
        self.reset_keys()
        self.handle_events()
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
        screen.fill((150, 150, 150))
        self.game.draw_text(
            screen,
            "DoL",
            (0, 0, 0),
            self.game.GAME_WIDTH / 2,
            self.game.GAME_HEIGHT / 2 -200,
        )
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