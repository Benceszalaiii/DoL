import os, time
import pygame as pg
# Load our scenes
from menu import Menu
from settings import WIDTH, HEIGHT

class Stack():
        def __init__(self):
            pg.init()
            self.SCREEN_WIDTH,self.SCREEN_HEIGHT = WIDTH, HEIGHT
            self.GAME_WIDTH, self.GAME_HEIGHT = self.SCREEN_WIDTH, self.SCREEN_HEIGHT
            self.screen = pg.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
            pg.display.set_caption("DoL - Loading..")
            self.running, self.playing = True, True
            self.actions = {"resume" : False, "pause" : False, "click" : False, "start" : False}
            self.dt, self.prev_time = 0, 0
            self.state_stack = []
            self.load_assets()
            self.load_states()
            self.logo = pg.image.load(os.path.join("assets", "logo.png"))
            pg.display.set_icon(self.logo)

        def game_loop(self):
            while self.playing:
                self.get_dt()
                self.get_events()
                self.update()
                self.render()
                time.sleep(1/100)

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
                if event.type == pg.KEYUP:
                    if event.key == pg.K_SPACE:
                        self.actions['resume'] = False
                    if event.key == pg.K_TAB:
                        self.actions['pause'] = False
                    if event.key == pg.K_RETURN:
                        self.actions['start'] = False  

        def update(self):
            self.state_stack[-1].update(self.dt,self.actions)

        def render(self):
            self.state_stack[-1].render(self.screen)
            # Render current state to the screen
            self.screen.blit(self.screen, (0, 0))
            pg.display.flip()


        def get_dt(self):
            now = time.time()
            self.dt = now - self.prev_time
            self.prev_time = now

        def draw_text(self, surface, text, color, x, y):
            text_surface = self.font.render(text, True, color)
            #text_surface.set_colorkey((0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            surface.blit(text_surface, text_rect)

        def load_assets(self):
            # Create pointers to directories 
            self.assets_dir = os.path.join("assets")
            self.sprite_dir = os.path.join(self.assets_dir, "sprites")
            self.font= pg.font.Font(os.path.join("DigitalDisco.ttf"), 20)

        def load_states(self):
            self.menu_screen = Menu(self)
            self.state_stack.append(self.menu_screen)

        def reset_keys(self):
            for action in self.actions:
                self.actions[action] = False


if __name__ == "__main__":
    g = Stack()
    while g.running:
        g.game_loop()