# THIS IS THE FILE FOR GLOBAL INPUTS

# ----------- #
#   IMPORTS   #
# ----------- #

import fusionengine as fe
import sys as kys

# ----------- #
#  FUNCTIONS  #
# ----------- #


def global_inputs(win: fe.Window) -> None:
    """
    Handles the inputs that handle the window

    - Exit
    - Switch screen
    """

# LEAVE GAME ON BACKSPACE
    if fe.key_down_once(fe.KEY_BACKSPACE):
        kys.exit()

# SWITCH MENU/GAME ON TAB
    if fe.key_down_once(fe.KEY_TAB):
        win.quit()
