# THIS IS THE FILE FOR GLOBAL INPUTS

# ----------- #
#   IMPORTS   #
# ----------- # 

import fusionengine as fe
from sys import exit as kys

# ----------- #
#  FUNCTIONS  #
# ----------- # 


def global_inputs(win: fe.Window) -> None:
    """
    Handles the inputs that handle the window
    
    - Exit
    - Switch screen
    """
    if fe.key_down_once(fe.KEY_R):
        kys()
    if fe.key_down_once(fe.KEY_ESCAPE):
        win.quit()