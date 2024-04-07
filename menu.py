from state import State
from game import Game
import pygame as pg
from button import Button
from inputs import global_inputs
print("Loading menu")


class Menu(State):
    def __init__(self, game):  # type: ignore
        State.__init__(self, game)
        self.title = "DoL - Main Menu"
        pg.display.set_caption(self.title)
        self.start = Button(x=self.game.GAME_WIDTH/2 - 100, y=self.game.GAME_HEIGHT/2 + 50, width=200,
                            height=100, text="Start", font_size=36, font_color=(0, 0, 0), background_color=(100, 100, 100))
        self.actions = {"start": False, "click": False}

    def update(self, delta_time: float):
        self.reset_keys()
        self.handle_events()
        self.start.update(self.actions["click"])
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("Click")
        if self.actions["click"]:
            print("Click clicked")
        if self.actions["start"]:
            new_state = Game(self.game)
            self.reset_keys()
            new_state.enter_state()


    def render(self, screen: pg.surface.Surface):
        screen.fill((255, 255, 255))
        self.game.draw_text(screen, "DoL", (0, 0, 0),
                            self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/2)

        self.start.render(screen)
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