# MAIN FILE TO RUN
from menu import Menu
from game import Game
from handler import Handler
import fusionengine as fe
from resolutions import Screen
# ------------- #
#  MAIN SCRIPT  #
# ------------- #


def main():
    run()


def run():
    screen = Screen()
    window = fe.Window("DoL Dodge of Legends", 1600, 900)
    menu = Menu(window, screen)
    needs_reset = False
    game_state = "menu"
    game = Game(window, screen, game_state)
    @window.loop
    def loop():
        if game_state == "menu":
            menu.run(game_state)
        elif game_state == "game":
            if needs_reset: 
                game = Game(window, screen, game_state)
            game.run()


if __name__ == "__main__":
    main()