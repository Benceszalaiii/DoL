__author__ = "Fusion Engine Team"
__version__ = "5.2.0"

import sys
import os
import warnings
import platform

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# Core
from fusionengine.engine.window import *
from fusionengine.engine.image import *
from fusionengine.engine.draw import *
from fusionengine.engine.shape import *

# Events
from fusionengine.engine.event import *
from fusionengine.engine.keys import *

# Colors
from fusionengine.engine.color import *

# Entity
from fusionengine.engine.entity import *

# Node
from fusionengine.engine.node import *

# Storage
from fusionengine.engine.storage import *

# UI
from fusionengine.engine.ui import *

# Math
from fusionengine.engine.vector import *
from fusionengine.engine.math import *

# Sound
from fusionengine.engine.sound import *

# Scene
from fusionengine.engine.scene import *
from fusionengine.engine.manager import *

# Tools
from fusionengine.engine.debug import *

# Animation
from fusionengine.engine.animation import *
from fusionengine.engine.spritesheets import *

# GL
import fusionengine.fusiongl as gl

import pygame as pg

