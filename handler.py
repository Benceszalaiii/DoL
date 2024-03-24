import fusionengine as fe
from resolutions import Screen
class Handler:
    def __init__(self) -> None:
        self.screen = Screen()
        self.win = fe.Window("DoL Dodge Of Legends", self.screen.current.width, self.screen.current.height)
        self.win.change_icon("logo.png")
        self.game_state = "menu"