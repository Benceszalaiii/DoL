import pygame as pg


class Choose_Button:
    def __init__(self, pos: tuple[int, int], size: int, option1: str, option2: str, text_color: tuple[int, int, int] = (255, 255,255)):
        self.font = pg.font.Font("League_font.ttf", 30)
        self.bg_rect = pg.Rect(pos, (size, size))
        self.bg_rect.center = pos
        self.option1 = option1
        self.option2 = option2
        self.option1_surf = self.font.render(self.option1, True, text_color)
        self.option2_surf = self.font.render(self.option2, True, text_color)
        self.opt1_rect = self.option1_surf.get_rect()
        self.opt2_rect = self.option2_surf.get_rect()
        self.active = self.option1_surf
        self.active_rect = self.opt1_rect
        self.active_rect.center = self.bg_rect.center
        self.active_value = self.option1

    def render(self, screen: pg.Surface):
        pg.draw.rect(screen, (0, 90, 130), self.bg_rect)
        screen.blit(self.active, self.active_rect)

    def update(self, actions: dict[str, bool]):
        if actions["click"]:
            self.handle_click()
    def handle_click(self):
        if self.bg_rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            if self.active == self.option1_surf:
                self.active = self.option2_surf
                self.active_value = self.option2
            else:
                self.active = self.option1_surf
                self.active_value = self.option1
            self.active_rect = self.active.get_rect()
            self.active_rect.center = self.bg_rect.center