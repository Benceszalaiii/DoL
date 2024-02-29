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
        if abs(self.player.x - self.destination.x) > abs(self.dx) and abs(self.player.y - self.destination.y) > abs(self.dy):
            self.player.x += self.p_speed * self.dx
            self.player.y += self.p_speed * self.dy

    def move_player(self, player: fusion.Node):
        dest_x, dest_y = fusion.get_mouse_pos(self)
        self.destination = fusion.Node(self.window, dest_x, dest_y, int(player.width / 2), int(player.height / 2))
        self.dx = dest_x - player.x
        self.dy = dest_y - player.y
        length = max(1, (self.dx ** 2 + self.dy ** 2) ** 0.5)
        self.dx /= length
        self.dy /= length
        print("DEST: ", dest_x, dest_y)
        self.walk()

    def distance(self, node1, node2):
        dx = node1.x - node2.x
        dy = node1.y - node2.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __init__(self):
        self.window.change_icon(fusion.DEBUGIMAGE)
        self.bg = fusion.Image("background.png", 0, 0, WIDTH, HEIGHT)

        @self.window.loop
        def loop():
            self.window.set_fps(FPS)
            self.bg.draw()
            self.player.load_rect(fusion.WHITE)
            self.destination.load_rect(fusion.PINK)
            self.destination.update()
            self.window_inputs()
            self.walk()
            print("CURR: ", self.player.x, self.player.y)
            self.player.update()
