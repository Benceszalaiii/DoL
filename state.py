# Parent class to handle states
import pygame as pg

print("Loading preset")


class State():
    def __init__(self, game):  # type: ignore
        self.game = game
        self.prev_state = None
        self.title = "DoL - Dodge Of Legends"
        self.actions = {}

    def update(self, delta_time: float):
        pass

    def render(self, screen: pg.surface.Surface):
        pass

    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)
        self.set_title()
        self.reset_keys()

    def exit_state(self):   # Basically kys command
        self.game.state_stack.pop()

    def set_title(self):
        pg.display.set_caption(self.title)

    def reset_keys(self):
        """
        Set all keys in self.actions to False
        """
        for key in self.actions:
            self.actions[key] = False
