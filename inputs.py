# THIS IS THE FILE FOR GLOBAL INPUTS

# ----------- #
#   IMPORTS   #
# ----------- #

import sys as kys  # KEY YOUR SHUTDOWN
import pygame as pg

# ----------- #
#  FUNCTIONS  #
# ----------- #


def global_inputs(event) -> None:  # type: ignore
    """
    Handles the inputs that handle the window

    - Exit
    """
    if event.type == pg.QUIT:
        pg.quit()
        kys.exit()

def exit() -> None:    # KYS COMMAND
    pg.quit()
    kys.exit()