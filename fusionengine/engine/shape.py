from fusionengine.engine.color import Color, BLUE
from fusionengine.engine.draw import draw_rect

import pygame as pg


class Rect:
    def __init__(
            self,
            rect: pg.Rect,
            color: Color
    ) -> None:
        """
        A class that creates a new rect shape.

        Args:
            x (int): X coordinate of the rect
            y (int): Y coordinate of the rect
            width (int): Width of the rect
            height (int): Height of the rect
            color (Color): Color of the rect
        """
        self.x = rect.x
        self.y = rect.y
        self.width = rect.width
        self.height = rect.height
        self.color = color
        self.rect = rect

    def draw(self) -> None:
        """
        Draw the rectangle
        """
        draw_rect(self.x, self.y, self.width, self.height, self.color)

    def get_rect(self) -> pg.Rect:
        return self.pg_rect
