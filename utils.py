from os import system as cmd

DEBUGMODE = False
# ----------- #
#   IMPORTS   #
# ----------- #

# ----------- #
#  FUNCTIONS  #
# ----------- #


def clr() -> None:
    """
    Clears the running CLI (command line interface)
    """
    if not DEBUGMODE:
        cmd("cls")


print("Utilities loaded")
