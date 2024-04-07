import pygame as pg
from state import State
from button import Button
from inputs import global_inputs

print("Loading settings menu")


class SettingsMenu(State):
    def __init__(self, game, config):  # type: ignore
        self.game = game
        self.title = "DoL - Currently Playing (Paused)"
        State.__init__(self, game, config)
        pg.display.set_caption(self.title)
        self.save_button = Button(
            x=self.game.screen_width / 2 - 100,
            y=self.game.screen_height - 200,
            width=200,
            height=100,
            text="Save",
            font_size=20,
            font_color=(200, 200, 200),
            background_color=(100, 100, 100),
            hover_font_color=(255, 255, 0),
            hover_background_color=(0, 255, 0),
        )
        self.volume_slider = Slider((700, 200), (300, 50), 0.7, 0, 100, self.game.font)
        self.actions = {"click": False}
        self.active_preferences = self.config.data

    def update(self, delta_time: float):
        self.inputs()
        self.save_button.update(self.actions["click"])
        self.update_slider()
        self.reset_keys()

    def render(self, screen: pg.surface.Surface):
        screen.fill((255, 255, 255))
        pg.display.flip()
        self.save_button.render(screen)
        self.game.draw_text(screen, "Volume", (0, 0, 0), 100, 200)
        self.volume_slider.render(screen)

    def update_slider(self):
        if (
            self.volume_slider.container_rect.collidepoint(pg.mouse.get_pos())
            and pg.mouse.get_pressed()[0]
        ):
            self.volume_slider.move_slider(pg.mouse.get_pos())
            self.config.volume = self.volume_slider.get_value()

    def inputs(self):
        for event in pg.event.get():
            global_inputs(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions["click"] = True
        if self.save_button.is_clicked:
            self.save_preferences()
            self.exit_state()

    def save_preferences(self):
        current_settings = self.config.data

        pass  # TODO: Save preferences


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
        self.font = font
        self.slider_left_pos = self.pos[0] - (size[0] // 2) + 5
        self.slider_right_pos = self.pos[0] + (size[0] // 2) + 5
        self.slider_top_pos = self.pos[1] - (size[1] // 2)

        self.min = min
        self.max = max
        self.initial_val = (
            self.slider_right_pos - self.slider_left_pos
        ) * initial_val  # <- %

        self.container_rect = pg.Rect(
            self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1]
        )
        self.button_rect = pg.Rect(
            self.slider_left_pos + self.initial_val - 5,
            self.slider_top_pos,
            20,
            self.size[1],
        )

    def move_slider(self, mouse_pos: tuple[int, int]):
        pos = mouse_pos[0]
        if pos < self.slider_left_pos:
            pos = self.slider_left_pos
        if pos > self.slider_right_pos:
            pos = self.slider_right_pos
        self.button_rect.centerx = pos

    def render(self, screen: pg.Surface):
        pg.draw.rect(screen, "darkgray", self.container_rect)
        pg.draw.rect(screen, "green", self.button_rect)
        screen.blit(self.font.render(str(int(self.get_value() * 1)), True, (255, 255, 255)), (self.button_rect.centerx, self.button_rect.centery))

    def get_value(self) -> float:
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        button_val = self.button_rect.centerx - self.slider_left_pos

        return (button_val / val_range) * (self.max - self.min) + self.min
