import pygame as pg
from state import State
from button import Button
from inputs import global_inputs
print("Loading settings menu")


class SettingsMenu(State):
    def __init__(self, game):  # type: ignore
        self.game = game
        self.title = "DoL - Currently Playing (Paused)"
        State.__init__(self, game)
        pg.display.set_caption(self.title)
        self.preferences: dict[str, str | bool] = {}
        self.lines = []
        self.save_button = Button(
            x=self.game.screen_width / 2 - 100,
            y=self.game.screen_height - 200,
            width=200,
            height=100,
            text="Save",
            font_size=20,
            font_color=(200, 200, 200),
            background_color=(100, 100, 100),
        )
        self.actions = {"click": False}

    def update(self, delta_time: float):
        self.inputs()
        self.save_button.update(self.actions["click"])
        self.reset_keys()

    def render(self, screen: pg.surface.Surface):
        screen.fill((255, 255, 255))
        pg.display.flip()
        self.save_button.render(screen)
        self.game.draw_text(screen, "Volume", (0, 0, 0), 100, 200)

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
        pass  # TODO

