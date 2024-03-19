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
    if fe.key_down_once(fe.KEY_ESCAPE):
        kys.exit()
    if fe.key_down_once(fe.KEY_R):
        win.quit()