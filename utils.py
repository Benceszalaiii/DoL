
# ----------- #
#   IMPORTS   #
# ----------- #

from os import system as cmd

# ----------- #
#  FUNCTIONS  #
# ----------- #

def empty_terminal(DEBUGMODE = 0) -> None:
    """
    Clears the running CLI (command line interface)
    """
    if not DEBUGMODE:
        pass
    else:
        cmd("cls")