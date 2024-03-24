# THIS IS THE FILE FOR GLOBAL INPUTS

# ----------- #
#   IMPORTS   #
# ----------- #

import sys as kys   # KEY YOUR SHUTDOWN
import fusionengine as fe

# ----------- #
#  FUNCTIONS  #
# ----------- #


def global_inputs() -> None:
    """
    Handles the inputs that handle the window
    
    - Exit
    """

# LEAVE GAME ON BACKSPACE
    if fe.key_down_once(fe.KEY_BACKSPACE):
        kys.exit()
