import pygame as pg
from config import Configuration
from state import State
from button import Button
from inputs import global_inputs

print("Loading pause")


class PauseMenu(State):
    def __init__(self, game, config):  # type: ignore
        self.game = game
        self.title = "DoL - Currently Playing (Paused)"
        State.__init__(self, game, config)
        pg.display.set_caption(self.title)
        self.button_width = self.game.screen_width / 5
        self.button_height = 75
        self.button_distance = 30
        self.resume = Button(
            x=self.game.screen_width / 2 - self.button_width / 2,
            y=self.game.screen_height / 3 + self.button_distance,
            width=self.button_width,
            height=self.button_height,
            text="Resume",
            font_size=20,
            font_color=(200, 200, 0),
            background_color=(3, 151, 171),
            hover_font_color=(200, 200, 200),
            hover_background_color=(0, 90, 130),
        )
        self.main_menu_button = Button(
            x=self.game.screen_width / 2 - self.button_width / 2,
            y=self.resume.rect.bottom + self.button_distance,
            width=self.button_width,
            height=self.button_height,
            text="Back to main menu",
            font_size=20,
            font_color=(200, 200, 200),
            background_color=(100, 100, 100),
            hover_font_color=(200, 200, 200),
            hover_background_color=(150, 0, 0),
        )
        self.actions = {"click": False}
        self.blur_amt = 0
        self.active = False

    def update(self, delta_time: float, config: Configuration):
        pg.display.set_caption(self.title)
        if self.active:
            self.inputs(config)
            self.resume.update(self.actions["click"])
            self.main_menu_button.update(self.actions["click"])
        self.reset_keys()

    def render(self, screen: pg.surface.Surface):
        if self.blur_amt < 36:
            try:
                screen.blit(pg.transform.box_blur(screen, 2), (0, 0))  # type: ignore
            except AttributeError:
                pass
            self.blur_amt += 2
        else:
            self.resume.render(screen)
            self.main_menu_button.render(screen)
        if self.blur_amt == 36:
            self.blur_amt += 1
            self.active = True
    def inputs(self, config: Configuration):
        for event in pg.event.get():
            global_inputs(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions["click"] = True
        if self.resume.is_clicked:
            self.exit_state()
        if self.main_menu_button.is_clicked:
            self.exit_state_twice(config)
