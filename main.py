from settings import WIDTH, HEIGHT
from menu import Menu
import pygame as pg
from utils import clr
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
        self.screen_width, self.screen_height = WIDTH, HEIGHT
        self.GAME_WIDTH, self.GAME_HEIGHT = self.screen_width, self.screen_height
        self.game_screen = pg.Surface((self.GAME_WIDTH, self.GAME_HEIGHT))
        self.screen = pg.display.set_mode(
            (self.screen_width, self.screen_height))
        self.FPS = pg.display.get_current_refresh_rate()
        pg.display.set_caption("DoL - Loading..")
        self.running, self.playing = True, True
        self.dt = time.time()
        self.prev_time = time.time()
        self.state_stack = []
        self.load_assets()
        self.load_states()
        self.logo = pg.image.load(os.path.join("assets", "logo.png"))
        pg.display.set_icon(self.logo)

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.update()
            self.render()
            self.mainClock.tick(self.FPS)

    def get_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.state_stack[-1].update(self.dt)

    def render(self):
        self.state_stack[-1].render(self.game_screen)
        # Render current state to the screen
        self.screen.blit(pg.transform.scale(
            self.game_screen, (self.screen.get_width(), self.screen.get_height())), (0, 0))
        pg.display.flip()


    def get_dt(self):
        self.dt = time.time() - self.prev_time
        self.dt *= self.FPS
        self.prev_time = time.time()

    def draw_text(self, surface: pg.surface.Surface, text: str, color: pg.Color, x: float, y: float):
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


if __name__ == "__main__":
    g = Stack()
    clr()
    print("Loading successful")
    print("Welcome to DoL")
    while g.running:
        g.game_loop()
