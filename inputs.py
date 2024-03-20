# THIS IS THE FILE FOR GLOBAL INPUTS

# ----------- #
#   IMPORTS   #
# ----------- #

import sys as kys
import fusionengine as fe

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
