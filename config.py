# THIS IS THE FILE FOR SETTINGS AND PREFERENCES

import json
import pygame as pg


class Configuration:
    def __init__(self):
        with open("preferences.json", "r") as f:
            self.data = json.load(f)
        self.click_preference = self.data["click"]
        self.flash_preference = self.data["flash"]
        self.resolutions = self.data["resolutions"]
        self.volume = self.data["volume"]
        self.width = self.data["width"]
        self.height = self.data["height"]
        self.speed = self.data["speed"]
        self.fps = self.data["fps"]
        self.handle_preferences()

    def __repr__(self) -> str:
        return str(self.data)

    def handle_preferences(self):
        if self.click_preference == "left":
            self.CLICK_KEY = 1
        elif self.click_preference == "right":
            self.CLICK_KEY = 3  #  type: ignore STUPID PYLANCE
        else:
            raise ValueError(
                "Unknown click preference, click must either be 'right' or 'left"
            )
        if self.flash_preference == "D":
            self.FLASH_KEY = pg.K_d
        elif self.flash_preference == "F":
            self.FLASH_KEY = pg.K_f  # type: ignore STUPID PYLANCE
        else:
            raise ValueError(
                "Unknown flash preference, flash must either be 'D' or 'F'"
            )

    def rewrite(self, new_dict):  # type: ignore Will not typehint all possibilities (int float string listlistint)
        with open("preferences.json", "w") as f:
            json.dump(new_dict, f, indent=4)

