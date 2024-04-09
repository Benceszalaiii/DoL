import pygame as pg
from config import Configuration
from state import State
from button import Button
from inputs import global_inputs
from toggle_button import ToggleButton
from slider import Slider
from option_button import Choose_Button

print("Loading settings menu")


class SettingsMenu(State):
    def __init__(self, game, config):  # type: ignore
        self.game = game
        self.title = "DoL - Browsing Settings"
        State.__init__(self, game, config)
        pg.display.set_caption(self.title)
        self.text_left = 400
        self.show_fps_button = ToggleButton((850, 500), 36, active=config.show_fps)
        self.save_button = Button(
            x=config.width / 2 - 100,
            y=config.height - 100,
            width=200,
            height=50,
            text="Save",
            font_size=20,
            font_color=(200, 200, 200),
            background_color=(9, 20, 40),
            hover_font_color=(200, 200, 200),
            hover_background_color=(0, 90, 130),
            outline=True,
            outline_color=(10, 200, 185),
            radius=-1,
        )
        self.volume_slider = Slider(
            (850, 175), (400, 50), config.volume, 0, 100, self.game.font
        )
        self.click_pref_button = Choose_Button(
            (850, 300), 75, config.click_preference, config.not_click
        )
        self.flash_pref_button = Choose_Button(
            (850, 400), 75, config.flash_preference, config.ghost_preference
        )
        self.elements_to_render = [  # type: ignore
            self.show_fps_button,
            self.save_button,
            self.volume_slider,
            self.flash_pref_button,
            self.click_pref_button,
        ]
        self.actions = {"click": False}

    def update(self, delta_time: float, config):  # type: ignore
        self.inputs(config)
        self.save_button.update(self.actions["click"])
        self.update_slider()
        self.show_fps_button.update(self.actions["click"])
        self.flash_pref_button.update(self.actions)
        self.click_pref_button.update(self.actions)
        self.reset_keys()

    def render(self, screen: pg.surface.Surface):
        screen.fill((9, 20, 40))
        self.game.draw_text(
            screen, "Settings", (200, 155, 60), self.config.width / 2, 100, 32
        )
        self.game.draw_text(screen, "Volume", (200, 135, 60), self.text_left, 175, 20)
        self.game.draw_text(
            screen, "Click Preference", (200, 155, 60), self.text_left, 300, 20
        )
        self.game.draw_text(
            screen, "Flash Preference", (200, 155, 60), self.text_left, 400, 20
        )
        self.game.draw_text(screen, "Show FPS", (200, 155, 60), self.text_left, 500, 20)
        for element in self.elements_to_render:  # type: ignore
            element.render(screen)

    def update_slider(self):
        if (
            self.volume_slider.container_rect.collidepoint(pg.mouse.get_pos())
            and pg.mouse.get_pressed()[0]
        ):
            self.volume_slider.move_slider(pg.mouse.get_pos())
            self.config.volume = self.volume_slider.get_value()

    def inputs(self, config: Configuration):
        for event in pg.event.get():
            global_inputs(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions["click"] = True
        if self.save_button.is_clicked:
            self.save_preferences(config)
            self.exit_state()

    def save_preferences(self, config: Configuration):
        config.volume = self.volume_slider.get_value()
        config.click_preference = self.click_pref_button.active_value
        config.flash_preference = self.flash_pref_button.active_value
        config.show_fps = self.show_fps_button.active
        config.rewrite()
