import pygame

import fusionengine as fusion
from settings import FPS, WIDTH, HEIGHT, TITLE


class Game(object):
    window: fusion.Window = fusion.Window(TITLE, WIDTH, HEIGHT)
    p_speed: int = 5
    player: fusion.Node = fusion.Node(window, 1, 1, 150, 150)
    dest_x: int = 509
    dest_y: int = 500
    dx: int = 0
    dy: int = 0

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
        if not self.player.x == self.dest_x and not self.player.y == self.dest_y:
            self.player.x += int(self.dx * self.p_speed)
            self.player.y += int(self.dy * self.p_speed)

    def move_player(self, player: fusion.Node):
        self.dest_x, self.dest_y = fusion.get_mouse_pos(self)
        self.dx = self.dest_x - player.x
        self.dy = self.dest_y - player.y
        length = max(1, (self.dx ** 2 + self.dy ** 2) ** 0.5)
        self.dx /= length
        self.dy /= length
        print("DEST: ", self.dest_x, self.dest_y)

        self.walk()

    def __init__(self):

        self.window.change_icon(fusion.DEBUGIMAGE)
        fusion.set_background_color(fusion.GRAY)

        @self.window.loop
        def loop():
            self.window.set_fps(FPS)
            self.player.load_rect(fusion.HOTPINK)
            self.window_inputs()
            self.walk()
            print("CURR: ", self.player.x, self.player.y)

            self.player.update()
