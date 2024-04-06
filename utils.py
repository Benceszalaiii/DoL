from os import system as cmd
import numpy as np
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


def sqrt(number: float):
    threehalfs = 1.5
    x2 = number * 0.5
    y = np.float32(number)
    i = y.view(np.int32)
    i = np.int32(0x5f3759df) - np.int32(i >> 1)  # what the fuck?
    y = i.view(np.float32)
    y = y * (threehalfs - (x2 * y * y))
    return float(y)


print(sqrt(16))
