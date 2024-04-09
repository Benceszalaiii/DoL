import pygame as pg
import os
import random


class Soundtrack:
    def __init__(self, volume: float):
        pg.mixer.init()
        self.music_ptr = os.path.join("assets", "music")
        self.menu_songs = []
        self.game_songs = []
        pg.mixer.music.set_volume(volume / 100)
        for song_name in os.listdir(self.music_ptr):
            if os.path.splitext(song_name)[1] == ".wav":
                if song_name[0:4] == "menu":
                    self.menu_songs.append(song_name)
                elif song_name[0:4] == "game":
                    self.game_songs.append(song_name)
        self.state = "menu"

    def start_menu(self):
        print("Starting menu")
        self.reset_state()
        self.state = "menu"
        random.shuffle(self.menu_songs)
        pg.mixer.music.load(os.path.join(self.music_ptr, self.menu_songs[0]))
        for song in self.menu_songs[1:]:
            pg.mixer.music.queue(os.path.join(self.music_ptr, song))
        pg.mixer.music.play()
        for _ in range(5):
            random.shuffle(self.menu_songs)
            for song in self.menu_songs:
                pg.mixer.music.queue(os.path.join(self.music_ptr, song))
    def start_game(self):
        self.reset_state()
        self.state = "game"
        random.shuffle(self.game_songs)
        pg.mixer.music.load(os.path.join(self.music_ptr, self.game_songs[0]))
        random.shuffle(self.game_songs)
        for song in self.game_songs[1:]:
            pg.mixer.music.queue(os.path.join(self.music_ptr, song))
        pg.mixer.music.play()

    def pause(self):
        pg.mixer.music.pause()

    def stop(self):
        pg.mixer.music.stop()
        pg.mixer.music.unload()

    def resume(self):
        pg.mixer.music.unpause()

    def set_volume(self, volume: float):
        if 0 <= volume <= 100:
            pg.mixer.music.set_volume(volume / 100)

    @property
    def volume(self):
        return round(pg.mixer.music.get_volume() * 100)

    def reset_state(self):
        pg.mixer.music.unload()
        self.stop()

    def update(self):
        if not pg.mixer.music.get_busy():
            if self.state == "menu":
                self.start_menu()
            elif self.state == "game":
                self.start_game()
