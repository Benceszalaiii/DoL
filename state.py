# Parent class to handle states
import pygame as pg
from config import Configuration
print("Loading preset")


class State:
    def __init__(self, game, config: Configuration):  # type: ignore
        self.game = game
        self.prev_state = None
        self.actions = {}
        self.config = config

    def update(self, delta_time: float):
        pass

    def render(self, screen: pg.surface.Surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)
        self.reset_keys()

    def exit_state(self):  # Basically kys command
        self.game.state_stack.pop()
    def exit_state_twice(self):
        self.game.state_stack.pop()
        self.game.state_stack.pop()

    def reset_keys(self):
        """
        Set all keys in self.actions to False
        """
        for key in self.actions:
            self.actions[key] = False
