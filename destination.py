# THIS IS THE FILE FOR THE DESTINATION NODE


# --------- #
#  IMPORTS  #
# --------- #

import fusionengine as fe
import pygame as pg


# ------------------- #
#         NODE        #
# ------------------- #

class Destination:

    # ------------------- #
    #   INITIALIZE NODE   #
    # ------------------- #

    def __init__(self, win, x, y, width, height):
        self.destination: fe.Node = fe.Node(win, x, y, width, height)
<<<<<<< HEAD
        self.rect = pg.Rect(self.destination.x, self.destination.y, self.destination.width, self.destination.height)
=======
        self.rect = pg.Rect(self.destination.x, self.destination.y,
                            self.destination.width, self.destination.height)
>>>>>>> 7d757a0a3e91729c06c254a54b998040cbf34cc7

    # ----------- #
    #   METHODS   #
    # ----------- #

# Handle coloring the hitbox

    def load_rect(self, col: fe.Color):
        self.destination.load_rect(col)
<<<<<<< HEAD

# Update the elements

    def update(self):
        self.rect.update(self.destination.x, self.destination.y, self.destination.width, self.destination.height)
=======


# Update the elements


    def update(self):
        self.rect.update(self.destination.x, self.destination.y,
                         self.destination.width, self.destination.height)
>>>>>>> 7d757a0a3e91729c06c254a54b998040cbf34cc7
        self.destination.update()
