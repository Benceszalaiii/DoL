from state import State
from game import Game
import pygame as pg
from button import Button

print("Loading menu")
class Menu(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.title = "DoL - Main Menu"
        pg.display.set_caption(self.title)
        self.start = Button(self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/2 + 50, 200, 100, text="Start", size=36, color=(0, 0, 0), rect_color=(100, 100, 100))

    def update(self, delta_time, actions):
        self.start.update(actions)
        if actions["start"]:
            new_state = Game(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, screen):
        screen.fill((255, 255, 255))
        self.game.draw_text(screen, "DoL", (0, 0, 0), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/2)

        self.start.render(screen)
