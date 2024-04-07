import pygame as pg
from state import State
from button import Button
from inputs import global_inputs

print("Loading pause")


class PauseMenu(State):
    def __init__(self, game):  # type: ignore
        self.game = game
        self.title = "DoL - Currently Playing (Paused)"
        State.__init__(self, game)
        pg.display.set_caption(self.title)
        self.resume = Button(
            x=self.game.screen_width / 2 - 100,
            y=self.game.screen_height / 2 - 100,
            width=200,
            height=100,
            text="Resume",
            font_size=20,
            font_color=(200, 200, 0),
            background_color=(100, 100, 100),
            hover_font_color=(200, 200, 200),
            hover_background_color=(100, 150, 150),
        )
        self.main_menu_button = Button(
            x=self.game.screen_width / 2 - 100,
            y=self.game.screen_height / 2 + 300,
            width=200,
            height=100,
            text="Back to main menu",
            font_size=20,
            font_color=(200, 200, 200),
            background_color=(100, 100, 100),
            hover_font_color=(100, 100, 100),
            hover_background_color=(200, 200, 200),
        )
        self.actions = {"click": False}

    def update(self, delta_time: float):
        self.inputs()
        self.resume.update(self.actions["click"])
        self.main_menu_button.update(self.actions["click"])
        self.reset_keys()

    def render(self, screen: pg.surface.Surface):
        self.resume.render(screen)
        self.main_menu_button.render(screen)

    def inputs(self):
        for event in pg.event.get():
            global_inputs(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions["click"] = True
        if self.resume.is_clicked:
            self.exit_state()
        if self.main_menu_button.is_clicked:
            self.exit_state_twice()
