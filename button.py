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
        self.font = pg.font.Font("DigitalDisco.ttf", self.font_size)
        self.text_surface = self.font.render(self.text, True, self.font_color)
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.hover_font_color = hover_font_color
        self.hover_backround_color = hover_background_color
        self.is_hovered = False
        self.is_clicked = False

    def render(self, screen: pg.surface.Surface) -> None:
        """
        Draws the button on the screen with centered text
        """
        if self.is_hovered:
            background_color = self.hover_backround_color
        else:
            background_color = self.background_color
        pg.draw.rect(screen, background_color, self.rect)
        text_x = self.rect.centerx - (self.text_surface.get_width() // 2)
        text_y = self.rect.centery - (self.text_surface.get_height() // 2)
        screen.blit(self.text_surface, (text_x, text_y))

    def update(self, click: bool) -> None:
        mouse_pos = pg.mouse.get_pos()
        self.check_hovered(mouse_pos)
        if self.is_hovered:
            self.text_surface = self.font.render(self.text, True, self.hover_font_color)
        self.check_clicked(mouse_pos, click)

    def check_hovered(self, pos: tuple[int, int]) -> None:
        """
        Checks if the button is clicked at a given position

        Args:
            pos (tuple): A tuple representing the mouse position (x, y)

        Returns:
            bool: True if the position is within the button's rectangle, False otherwise
        """
        self.is_hovered = self.rect.collidepoint(pos)

    def check_clicked(self, pos: tuple[int, int], click: bool) -> None:
        if click and self.is_hovered:
            self.is_clicked = True
        else:
            self.is_clicked = False