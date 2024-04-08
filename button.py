import pygame as pg


class Button:
    """
    A button that can be clicked
    """

    def __init__(
        self,
        *,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        font_size: int,
        font_color: tuple[int, int, int],
        background_color: tuple[int, int, int],
        hover_font_color: tuple[int, int, int],
        hover_background_color: tuple[int, int, int],
        cooler: bool = False,
        cooler_color: tuple[int, int, int] = (52, 60, 95),
    ):
        """
        Initializes a button object
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color
        self.font = pg.font.Font("League_font.ttf", self.font_size)
        self.text_surface = self.font.render(self.text, True, self.font_color)
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.hover_font_color = hover_font_color
        self.hover_backround_color = hover_background_color
        self.is_hovered = False
        self.is_clicked = False
        self.elevation = height / 12
        self.dynamic_elevation = self.elevation
        self.original_y_pos = self.y
        self.elevation_rect = pg.Rect(self.x, self.y, self.width, self.elevation)
        self.elevation_color = cooler_color
        self.border_radius = 12
        self.cooler = cooler
        if self.cooler:
            self.whole_rect = pg.Rect(
                self.x , self.y - self.elevation, self.width, self.height + self.elevation
            )
        else:
            self.whole_rect = self.rect

    def render(self, screen: pg.surface.Surface) -> None:
        """
        Draws the button on the screen with centered text
        """
        if self.is_hovered:
            background_color = self.hover_backround_color
        else:
            background_color = self.background_color
        if self.cooler:
            pg.draw.rect(
                screen,
                self.elevation_color,
                self.elevation_rect,
                border_radius=self.border_radius,
            )
        pg.draw.rect(
            screen, background_color, self.rect, border_radius=self.border_radius
        )
        text_x = self.rect.centerx - (self.text_surface.get_width() // 2)
        text_y = self.rect.centery - (self.text_surface.get_height() // 2)
        screen.blit(self.text_surface, (text_x, text_y))

    def update(self, click: bool) -> None:
        mouse_pos = pg.mouse.get_pos()
        self.check_hovered(mouse_pos)
        if self.is_hovered:
            self.text_surface = self.font.render(self.text, True, self.hover_font_color)
        self.check_clicked(mouse_pos, click)
        if self.cooler:
            self.rect.y = self.original_y_pos - self.dynamic_elevation
        if self.is_hovered:
            self.dynamic_elevation = 0
        else:
            self.dynamic_elevation = self.elevation
        self.elevation_rect.midtop = self.rect.midtop
        self.elevation_rect.height = self.rect.height + self.dynamic_elevation

    def check_hovered(self, pos: tuple[int, int]) -> None:
        """
        Checks if the button is clicked at a given position

        Args:
            pos (tuple): A tuple representing the mouse position (x, y)

        Returns:
            bool: True if the position is within the button's rectangle, False otherwise
        """
        self.is_hovered = self.whole_rect.collidepoint(pos)

    def check_clicked(self, pos: tuple[int, int], click: bool) -> None:
        if click and self.is_hovered:
            self.is_clicked = True
        else:
            self.is_clicked = False
