import pygame as pg


class Button:
    """
    A button that can be clicked
    """

    def __init__(self, screen, x: int, y: int, width: int, height: int, text: str, font_size: int, font_color: tuple, background_color: tuple, on_click=None):
        """
        Initializes a button object
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color
        self.font = pygame.font.Font(None, self.font_size)
        self.text_surface = self.font.render(self.text, True, self.font_color)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.on_click = on_click

    def render(self):
        """
        Draws the button on the screen with centered text
        """
        pygame.draw.rect(self.screen, self.background_color, self.rect)
        text_x = self.rect.centerx - (self.text_surface.get_width() // 2)
        text_y = self.rect.centery - (self.text_surface.get_height() // 2)
        self.screen.blit(self.text_surface, (text_x, text_y))

    def is_clicked(self, pos):
        """
        Checks if the button is clicked at a given position

        Args:
            pos (tuple): A tuple representing the mouse position (x, y)

        Returns:
            bool: True if the position is within the button's rectangle, False otherwise
        """
        return self.rect.collidepoint(pos)

    def handle_event(self, event):
        """
        Handles mouse events for the button.

        Args:
            event (pygame.event): A pygame event object.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.is_clicked(event.pos):
            if self.on_click:
                self.on_click()


Button()
