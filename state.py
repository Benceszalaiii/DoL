# Parent class to handle states
import pygame as pg

class State():
    def __init__(self, game):
        self.game = game
        self.prev_state = None

    def update(self, delta_time, actions):
        pass

    def render(self, screen):
        pass


    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)
    def exit_state(self):   # Basically kys command
        self.set_title()
        self.game.state_stack.pop()

    def set_title(self):
        pg.display.set_caption(self.prev_state.title)