DEBUGMODE = True
# ----------- #
#   IMPORTS   #
# ----------- #

from os import system as cmd
# ----------- #
#  FUNCTIONS  #
# ----------- #

def empty_terminal() -> None:
    """
    Clears the running CLI (command line interface)
    """
    if not DEBUGMODE:
        cmd("cls")
print("Utilities loaded")
