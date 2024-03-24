# THIS IS THE FILE FOR SESSION MANAGEMENT

# ----------- #
#   IMPORTS   #
# ----------- #
from menu import Menu
from game import Game
from handler import Handler
# ----------------- #
#  SESSION MANAGER  #
# ----------------- #
def run():
    handler = Handler()
    menu = Menu(handler)
    needs_reset = False
    @handler.win.loop
    def loop():
        if handler.game_state == "menu":
            menu.run(handler)
        elif handler.game_state == "game":
            game = Game(Handler)
            if needs_reset: 
                game = Game(Handler)
            game.run(handler)
