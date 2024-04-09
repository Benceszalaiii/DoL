import pygame as pg
from state import State
from button import Button
from inputs import global_inputs
from toggle_button import ToggleButton
from slider import Slider
print("Loading settings menu")


class SettingsMenu(State):
    def __init__(self, game, config):  # type: ignore
        self.game = game
        self.title = "DoL - Currently Playing (Paused)"
        State.__init__(self, game, config)
        pg.display.set_caption(self.title)
        self.toggle_button = ToggleButton((800, 100), 36)
        self.save_button = Button(
            x=config.width / 2 - 100,
            y=config.height - 200,
            width=200,
            height=75,
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
            (700, 200), (400, 50), config.volume, 0, 100, self.game.font
        )
        self.actions = {"click": False}
        self.active_preferences = self.config.data

    def update(self, delta_time: float, config):  # type: ignore
        self.inputs()
        self.save_button.update(self.actions["click"])
        self.update_slider()
        self.toggle_button.update(self.actions["click"])
        self.reset_keys()

    def render(self, screen: pg.surface.Surface):
        screen.fill((9, 20, 40))
        self.save_button.render(screen)
        self.game.draw_text(screen, "Volume", (200, 155, 60), 100, 200)
        self.volume_slider.render(screen)
        self.toggle_button.render(screen)

    def update_slider(self):
        if (
            self.volume_slider.container_rect.collidepoint(pg.mouse.get_pos())
            and pg.mouse.get_pressed()[0]
        ):
            self.volume_slider.move_slider(pg.mouse.get_pos())
            self.config.volume = self.volume_slider.get_value()

    def inputs(self):
        for event in pg.event.get():
            global_inputs(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions["click"] = True
        if self.save_button.is_clicked:
            self.save_preferences()
            self.exit_state()

    def save_preferences(self):
        # current_settings = self.config.data

        pass  # TODO: Save preferences

