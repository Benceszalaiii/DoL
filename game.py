import math

import fusionengine as fusion
import pygame
from settings import FPS, WIDTH, HEIGHT, TITLE


class Game(object):
    window: fusion.Window = fusion.Window(TITLE, WIDTH, HEIGHT)
    p_speed: int = 5
    player: fusion.Node = fusion.Node(window, 1, 1, 150, 150)
    dx: float = 0
    dy: float = 0
    destination: fusion.Node = fusion.Node(window, player.x, player.y, 75, 75)
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
    destination_rect = pygame.Rect(
        destination.x, destination.y, destination.width, destination.height)
    ground_arow_sh = fusion.SpriteSheet("./ground_arrows.png", 16, 16)
    ground_arrow_an = fusion.Animation(window, ground_arow_sh, 1 / 3)

    def window_inputs(self):
        if fusion.key_down_once(fusion.KEY_F1):
            self.window.toggle_fullscreen()
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
        ev = pygame.event.get()
        for event in ev:
            if pygame.mouse.get_pressed()[0]:
                self.move_player(self.player)
            if event.type == pygame.QUIT:
                self.window.quit()

    def walk(self):
        if not self.destination_rect.colliderect(self.player_rect):
            self.player.x += self.p_speed * self.dx
            self.player.y += self.p_speed * self.dy

    def move_player(self, player: fusion.Node):
        dest_x, dest_y = fusion.get_mouse_pos(self)
        self.destination = fusion.Node(self.window, dest_x, dest_y, int(
            player.width / 2), int(player.height / 2))
        self.dx = dest_x - player.x
        self.dy = dest_y - player.y
        length = max(1, (self.dx ** 2 + self.dy ** 2) ** 0.5)
        self.dx /= length
        self.dy /= length

    def __init__(self):
        self.window.change_icon("logo.png")
        self.bg = fusion.Image("background.jpg", 0, 0, WIDTH, HEIGHT)

        @self.window.loop
        def loop():
            self.window.set_fps(FPS)
            self.player.load_rect(fusion.BLUE)
            self.bg.draw()
            self.destination.load_rect(fusion.RED)
            # self.destination_rect.load_animation(self.ground_arrow_an)
            self.window_inputs()
            self.walk()
            self.player_rect.update(
                self.player.x, self.player.y, self.player.width, self.player.height)
            self.destination_rect.update(
                self.destination.x, self.destination.y, self.destination.width, self.destination.height)
            print(self.destination_rect.x, self.destination_rect.y)
            self.destination.update()
            self.player.update()
