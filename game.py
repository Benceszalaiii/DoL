# Itt kell szerintem valaminek lenni, találtam egy random # jelet, szoval ideirom hogy valamit kellene vele kezdeni
from typing import Any
import pygame as pg

import fusionengine as fusion
from settings import FPS, WIDTH, HEIGHT, TITLE
import sys
import utils
class Game:

    def window_inputs(self):
        if fusion.key_down_once(fusion.KEY_F1):
            self.window.toggle_fullscreen()
            screen = utils.screen_size()
            self.window.width = screen["width"]
            self.window.height = screen["height"]
        if fusion.key_down_once(fusion.KEY_ESCAPE):
            self.window.quit()
        if fusion.key_down(fusion.KEY_D):
            self.player.x += 20
        elif fusion.key_down(fusion.KEY_A):
            self.player.x -= 20
        if fusion.key_down(fusion.KEY_S):
            self.player.y += 20
        elif fusion.key_down(fusion.KEY_W):
            self.player.y -= 20
        ev = pg.event.get()
        for event in ev:
            if pg.mouse.get_pressed()[0]:
                self.move_player(self.player_f)
            if event.type == pg.QUIT:
                print("We wish to see you again!")
                sys.exit()

    def walk(self):
        if not self.destination_rect.colliderect(self.player_rect):
            self.player_f.x += self.p_speed * self.dx
            self.player_f.y += self.p_speed * self.dy

    def move_player(self, player: fusion.Node):
        dest_x, dest_y = fusion.get_mouse_pos(self)
        self.destination.x = dest_x
        self.destination.y = dest_y
        self.dx = dest_x - player.x
        self.dy = dest_y - player.y
        length = max(1, (self.dx ** 2 + self.dy ** 2) ** 0.5)
        self.dx /= length
        self.dy /= length

    def __init__(self, win):
        self.window: fusion.Window = win
        self.window._running = True
        self.p_speed: int = 5
        self.player: fusion.Node = fusion.Node(self.window, self.window.width, self.window.height, 150, 150)
        self.player_f = fusion.Node(self.window, self.player.x/2 - 5, self.player.y/2 - 5, 10, 10)
        self.dx: float = 0
        self.dy: float = 0
        self.destination: fusion.Node = fusion.Node(self.window, self.player_f.x, self.player_f.y, 10, 10)
        self.player_rect = pg.Rect(self.player_f.x, self.player_f.y, self.player_f.width, self.player_f.height)
        self.destination_rect = pg.Rect(self.destination.x, self.destination.y, self.destination.width, self.destination.height)

        self.ground_arow_sh = fusion.SpriteSheet("./ground_arrows.png", 16, 16)
        self.ground_arrow_an = fusion.Animation(self.window, self.ground_arow_sh, 1 / 3)
        print("Switching to game")

    def run(self):
        self.window.change_icon("logo.png")
        self.bg = fusion.Image("background.jpg", 0, 0, WIDTH, HEIGHT)
        @self.window.loop
        def loop():
            self.player_f.load_rect(fusion.ORANGERED)
            self.window.set_fps(FPS)
            self.bg.draw()
            self.player.load_rect( fusion.WHITE)
            self.destination.load_rect( fusion.PINK)
                #self.destination_rect.load_animation(self.ground_arrow_an)
            self.player.update()
            self.player_f.update()
            self.window_inputs()
            self.walk()
            self.player_rect.update(self.player_f.x, self.player_f.y, self.player_f.width, self.player_f.height)
            self.destination_rect.update(self.destination.x, self.destination.y, self.destination.width, self.destination.height)
            print(self.destination_rect.x, self.destination_rect.y)
            self.player.x = self.player_f.x - self.player.width/2
            self.player.y = self.player_f.y - self.player.height/2

            self.destination.update()
