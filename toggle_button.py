import pygame as pg


class ToggleButton:
    def __init__(
        self,
        pos: tuple[int, int],
        size: int,
        active_color: tuple[int, int, int] = (200, 155, 60),
        inactive_color: tuple[int, int, int] = (18, 40, 80),
        outline_color: tuple[int, int, int] = ( 205, 250, 250),
        active: bool = False
    ):
        self.x, self.y = pos
        self.size = size
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.rect = pg.Rect(self.x, self.y, self.size /4 * 3, self.size /4*3)
        self.rect.center = (self.x, self.y)
        self.outline_color = outline_color
        self.bg_rect = pg.Rect(self.x, self.y, self.size, self.size)
        self.bg_rect.center = (self.x, self.y)
        self.active = active
        self.base_rect = pg.Rect(self.x, self.y, self.size, self.size)
        self.base_rect.center = (self.x, self.y)

    def update(self, clicked: bool):
        if self.rect.collidepoint(pg.mouse.get_pos()) and clicked:
            self.active = not self.active

    def render(self, screen: pg.Surface):
        pg.draw.rect(screen, self.inactive_color, self.base_rect)
        pg.draw.rect(screen, self.outline_color, self.bg_rect, width = 4)
        if self.active:
            pg.draw.rect(screen, self.active_color, self.rect)
        else:
            pg.draw.rect(screen, self.inactive_color, self.rect)
