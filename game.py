import pygame
import math
import fusionengine as fusion
from settings import FPS, WIDTH, HEIGHT, TITLE


class Game(object):
    window: fusion.Window = fusion.Window(TITLE, WIDTH, HEIGHT)
    p_speed: int = 5
    player: fusion.Node = fusion.Node(window, 1, 1, 150, 150)
    dest_x: int = 509
    dest_y: int = 500
    dx: float = 1
    dy: float = 1
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
        if self.player.get_coord_tuple() != self.destination.get_coord_tuple():
            self.player.x += int(self.dx * self.p_speed)
            self.player.y += int(self.dy * self.p_speed)

    def move_player(self, player: fusion.Node):
        self.dest_x, self.dest_y = fusion.get_mouse_pos(self)
        self.destination = fusion.Node(self.window, self.dest_x, self.dest_y, int(player.width/2), int(player.height/2))
        self.dx = self.dest_x - player.x - (player.width / 2)
        self.dy = self.dest_y - player.y - (player.height / 2)
        length = max(1, (self.dx ** 2 + self.dy ** 2) ** 0.5)
        self.dx /= length
        self.dy /= length
        print("DEST: ", self.dest_x, self.dest_y)
        self.walk()

    def distance(self, node1, node2):
        dx = node1.x - node2.x
        dy = node1.y - node2.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def check_collision(self, node1, node2):
        def check_collision(node1, node2):
            radius_sum = node1.radius + node2.radius
            return self.distance(node1, node2) < radius_sum
    def __init__(self):
        self.window.change_icon(fusion.DEBUGIMAGE)
        fusion.set_background_color(fusion.BLACK)

        @self.window.loop
        def loop():
            self.window.set_fps(FPS)
            self.player.load_rect(fusion.WHITE)
            self.window_inputs()
            self.walk()

            print("CURR: ", self.player.x, self.player.y)
            self.player.update()
