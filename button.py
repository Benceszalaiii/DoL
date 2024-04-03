import pygame as pg

class Button:
    def __init__(self, x, y, width, height, *, text="DEBUGTEXT", size=36, font="DigitalDisco.ttf", color=(255, 255, 255), rect_color=(100, 100, 100)):
        pg.init()
        self.color = color
        self.text = pg.font.Font(font, size).render(text, True, self.color)
        self.rect = self.text.get_rect()
        self.rect.center = (x, y)
        self.rect_color = rect_color
        self.text_content = text
    def update(self, actions):
        if actions["click"]:
            self.check_click(actions)

    def render(self, screen):
        pg.draw.rect(screen, self.rect_color, self.rect)
        screen.blit(self.text, self.rect)
    def check_click(self, actions):
        if self.rect.topleft[0] < pg.mouse.get_pos()[0] < self.rect.topright[0] and self.rect.topleft[1] < pg.mouse.get_pos()[1] < self.rect.bottomleft[1]:
            print("Clicked")
            actions["start"] = True