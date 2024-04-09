import pygame as pg
from config import Configuration
from state import State
from button import Button
from inputs import global_inputs
import os

print("Loading pause")


class Deathscreen(State):
    def __init__(self, game, config):  # type: ignore
        self.game = game
        self.title = "DoL - Death screen"
        State.__init__(self, game, config)
        self.button_width = self.game.screen_width / 5
        self.button_height = 75
        self.button_distance = 30
        self.main_menu_button = Button(
            x=config.width / 2 - self.button_width / 2,
            y=600,
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
        self.death_model = pg.transform.scale(
            (pg.image.load(os.path.join("assets", "death_screen.png")).convert_alpha()),
            (config.width, config.height),
        )
        self.death_rect = self.death_model.get_rect()
        self.death_rect.center = (self.game.GAME_WIDTH / 2, self.game.GAME_HEIGHT / 2)
        self.opacity_amt = 0
        # pg.mouse.set_visible(True)

    def update(self, delta_time: float, config: Configuration):
        pg.display.set_caption(self.title)
        self.inputs(config)
        self.main_menu_button.update(self.actions["click"])
        self.reset_keys()

    def render(self, screen: pg.surface.Surface):
        if self.opacity_amt <= 100:
            self.opacity_amt = min(100, self.opacity_amt + 0.5)
            self.death_model.set_alpha(int(self.opacity_amt))
        screen.blit(self.death_model, self.death_rect)
        if self.opacity_amt == 100:
            self.main_menu_button.render(screen)

    def inputs(self, config: Configuration):
        for event in pg.event.get():
            global_inputs(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions["click"] = True
        if self.main_menu_button.is_clicked:
            self.exit_state_twice(config)
