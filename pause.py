import pygame as pg
from state import State
from button import Button
print("Loading pause")


class PauseMenu(State):
    def __init__(self, game):  # type: ignore
        self.game = game
        self.title = "DoL - Currently Playing (Paused)"
        State.__init__(self, game)
        pg.display.set_caption(self.title)
        self.resume = Button(self.game.screen_width/2 - 100, self.game.screen_height/2,
                             200, 100,  "Resume", 20, (200, 200, 200), (100, 100, 100))
        self.actions = {"click": False}

    def update(self, delta_time: float):
        self.inputs()
        self.resume.update(self.actions["click"])
        self.reset_keys()

    def render(self, screen: pg.surface.Surface):
        self.resume.render(screen)

    def inputs(self):
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions["click"] = True
        if self.resume.is_clicked:
            self.exit_state()