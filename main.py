from settings import WIDTH, HEIGHT, FPS
from menu import Menu
import pygame as pg
from utils import empty_terminal
import contextlib
import time
import os
print("Loading module: os")
print("Loading module: time")
print("Loading module: contextlib")
with contextlib.redirect_stdout(None):
    import pygame as pg
# Load our scenes

print("Starting game..")


class Stack:
    def __init__(self):
        pg.init()
        self.mainClock = pg.time.Clock()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = WIDTH, HEIGHT
        self.GAME_WIDTH, self.GAME_HEIGHT = self.SCREEN_WIDTH, self.SCREEN_HEIGHT
        self.game_screen = pg.Surface((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.screen = pg.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pg.display.set_caption("DoL - Loading..")
        self.running, self.playing = True, True
        self.actions = {"resume": False, "pause": False, "click": False,
                        "start": False, "recent_resize": False, "resize": False, "resize": False}
        self.dt = time.time()
        self.prev_time = time.time()
        self.state_stack = []
        self.load_assets()
        self.load_states()
        self.logo = pg.image.load(os.path.join("assets", "logo.png"))
        pg.display.set_icon(self.logo)
        self.new_res = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()
            self.mainClock.tick(FPS)

    def get_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.actions["click"] = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pg.K_SPACE:
                    self.actions['resume'] = True
                if event.key == pg.K_TAB:
                    self.actions['pause'] = True
                if event.key == pg.K_RETURN:
                    self.actions['start'] = True
                if event.key == pg.K_1:
                    if not self.actions['recent_resize']:
                        self.actions['recent_resize'] = True
                        self.actions['resize'] = True
                        self.new_res = (1600, 900)
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.actions['resume'] = False
                if event.key == pg.K_TAB:
                    self.actions['pause'] = False
                if event.key == pg.K_RETURN:
                    self.actions['start'] = False

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def render(self):
        self.state_stack[-1].render(self.game_screen)
        # Render current state to the screen
        self.screen.blit(pg.transform.scale(
            self.game_screen, (self.screen.get_width(), self.screen.get_height())), (0, 0))
        pg.display.flip()

    def check_resize(self):
        if not self.actions['recent_resize'] and self.new_res != (self.SCREEN_WIDTH, self.SCREEN_HEIGHT):
            self.actions['resize'] = False
            self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.new_res
            self.screen = pg.display.set_mode(
                (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def get_dt(self):
        self.dt = time.time() - self.prev_time
        self.dt *= FPS
        self.prev_time = time.time()

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        # text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def load_assets(self):
        # Create pointers to directories
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font = pg.font.Font(os.path.join("DigitalDisco.ttf"), 20)

    def load_states(self):
        self.menu_screen = Menu(self)
        self.state_stack.append(self.menu_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False


if __name__ == "__main__":
    g = Stack()
    empty_terminal()
    print("Loading successful")
    print("Welcome to DoL")
    while g.running:
        g.game_loop()
