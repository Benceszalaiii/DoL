from state import State
from game import Game
import pygame as pg
class Menu(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.title = "DoL - Main Menu"
        pg.display.set_caption(self.title)
    def update(self, delta_time, actions):
        if actions["start"]:
            new_state = Game(self.game)
            new_state.enter_state()
        self.game.reset_keys()
        
    def render(self, display):
        display.fill((255, 255, 255))
        self.game.draw_text(display, "DoL", (0, 0, 0), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/2)