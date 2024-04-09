import pygame as pg
import os


class Slider:
    def __init__(
        self,
        pos: tuple[int, int],
        size: tuple[int, int],
        initial_val: float,
        min: int,
        max: int,
        font: pg.font.Font,
    ) -> None:
        self.pos = pos
        self.size = size
        self.hovered = False
        self.grabbed = False
        self.font = pg.font.Font(os.path.join("League_font.ttf"), 48)
        self.slider_left_pos = self.pos[0] - (size[0] // 2)
        self.slider_right_pos = self.pos[0] + (size[0] // 2)
        self.slider_top_pos = self.pos[1] - (size[1] // 2)
        self.initial_val = initial_val
        self.min = min
        self.max = max
        self.initial_pos = int(
            (self.slider_right_pos - self.slider_left_pos) * initial_val / 100
        )  # <- %

        self.container_rect = pg.Rect(
            self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1]
        )
        self.button_rect = pg.Rect(
            self.slider_left_pos + self.initial_pos - 3,
            self.slider_top_pos,
            20,
            self.size[1],
        )
        if self.initial_pos > self.container_rect.right:
            self.initial_pos = self.container_rect.right

    def move_slider(self, mouse_pos: tuple[int, int]):
        pos = mouse_pos[0]
        if pos < self.slider_left_pos:
            pos = self.slider_left_pos
        if pos > self.slider_right_pos:
            pos = self.slider_right_pos
        self.button_rect.x = pos

    def render(self, screen: pg.Surface):
        pg.draw.rect(screen, (9, 20, 40), self.container_rect)
        pg.draw.rect(screen, (120, 90, 40), self.button_rect)
        screen.blit(
            self.font.render(str(int(self.get_value() * 1)), True, (255, 255, 255)),
            (
                self.container_rect.right + 50,
                self.container_rect.centery - self.container_rect.height + 15,
            ),
        )
        self.outline_pos = (
            (self.container_rect.x - 5, self.container_rect.y),  # Top left
            (
                self.container_rect.x
                + self.container_rect.width
                + self.button_rect.width,
                self.container_rect.y,
            ),  # Top right
            (
                self.container_rect.x
                + self.container_rect.width
                + self.button_rect.width,
                self.container_rect.y + self.container_rect.height,
            ),  #  Bottom right
            (
                self.container_rect.x - 5,
                self.container_rect.y + self.container_rect.height,
            ),
        )  # Bottom left
        pg.draw.lines(
            screen,
            (240, 240, 255),
            True,
            (self.outline_pos),  # type: ignore
            2,
        )

    def get_value(self) -> float:
        val_range = self.slider_right_pos - self.slider_left_pos
        button_val = self.button_rect.centerx - self.slider_left_pos
        result = abs(
            round((button_val / val_range) * (self.max - self.min) + self.min - 2)
        )
        return 100 if result > 100 else result
