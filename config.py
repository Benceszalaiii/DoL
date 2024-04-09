# THIS IS THE FILE FOR SETTINGS AND PREFERENCES

import json
import pygame as pg


class Configuration:
    def __init__(self):
        with open("preferences.json", "r") as f:
            self.data = json.load(f)
        self.click_preference = self.data["click"]
        self.flash_preference = self.data["flash"]
        self.not_click = "LEFT" if self.click_preference == "RIGHT" else "RIGHT"
        self.volume = self.data["volume"]
        self.width = self.data["width"]
        self.height = self.data["height"]
        self.speed = self.data["speed"]
        self.fps = self.data["fps"]
        self.show_fps = self.data["show_fps"]
        self.easter_egg = self.data["easter_egg"]
        self.pause_quitted = False
        self.handle_preferences()



    def handle_preferences(self):
        if self.click_preference.lower() == "left":   # type: ignore
            self.CLICK_KEY = 1
            self.not_click = "RIGHT"
        elif self.click_preference.lower() == "right":  # type: ignore
            self.CLICK_KEY = 3  #  type: ignore STUPID PYLANCE
            self.not_click = "LEFT"
        else:
            raise ValueError(
                "Unknown click preference, click must either be 'right' or 'left"
            )
        if self.flash_preference.lower() == "d":
            self.ghost_preference = "F"
            self.FLASH_KEY = pg.K_d
            self.GHOST_KEY = pg.K_f
        elif self.flash_preference.lower() == "f":  # type: ignore
            self.ghost_preference = "D"
            self.FLASH_KEY = pg.K_f  # type: ignore STUPID PYLANCE
            self.GHOST_KEY = pg.K_d  # type: ignore STUPID PYLANCE
        else:
            raise ValueError(
                "Unknown flash preference, flash must either be 'D' or 'F'"
            )
    def reload(self):
        self.click_preference = self.data["click"]
        self.flash_preference = self.data["flash"]
        self.volume = self.data["volume"]
        self.handle_preferences()
    def rewrite(self):  # type: ignore Will not typehint all possibilities (int float string listlistint)
        new_dict: dict[str, bool|int|float|str] = {
            "click": self.click_preference,
            "flash": self.flash_preference,
            "volume": self.volume,
            "show_fps": self.show_fps,
        }
        self.data.update(new_dict)
        with open("preferences.json", "w") as f:
            json.dump(self.data, f, indent=4)
        self.reload()