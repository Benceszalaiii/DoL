# ----------- #
#   IMPORTS   #
# ----------- #
import tkinter
import gc
from config import RESOLUTIONS, WIDTH, HEIGHT
# ----------- #
#  FUNCTIONS  #
# ----------- #


class Resolution:
    """
    Stores details about a resolution (width, height) as integers

    Methods:
        initialize -> arguments: width, height
        get_resolution -> returns with tuple(width, height)             -- property
        as_str -> returns with string formatted resolution ("1600x900") -- property
    """

    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h

    @property
    def get_resolution(self):
        """
        Returns width and height as a tuple(width: int, height: int)

        Example:
        width: 1600, height: 900 --> (1600, 900)
        """
        return (self.width, self.height)

    @property
    def as_str(self) -> str:
        """
        Returns resolution as string

        Example:
            width: 1600, height: 900 --> "1600x900"
        """
        return str(self.width) + "x" + str(self.height)


class Screen:
    def __init__(self):
        self.max_res: Resolution = self.screen_size()
        self.resolutions: list[Resolution] = [self.max_res]
        self._available_resolutions()
        self.collect_garbage()
        self.current: Resolution = Resolution(WIDTH, HEIGHT)
        self.previous: Resolution
        self.offset_x: int = 0
        self.offset_y: int = 0

    # Get active screen's resolution
    def screen_size(self) -> Resolution:
        """
        Get the current screen's dimensions
        Returns with a Resolution object
        """
        root = tkinter.Tk()  # Initialize TCL interpreter
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.quit()  # Quit TCL interpeter, freeing up memory
        return Resolution(w, h)  # Get screen resolution, return it

    def _available_resolutions(self) -> list[Resolution] | None:
        global RESOLUTIONS
        for res in RESOLUTIONS:
            w, h = res[0], res[1]
            if not w > self.max_res.width and not h > self.max_res.height:
                check_res = Resolution(w, h)
                if self.max_res.get_resolution != check_res.get_resolution:
                    self.resolutions.append(check_res)

    @property
    def get_offset(self) -> None:
        """
        Gets the offset of the screen compared to previous resolution in pixels
        """
        self.offset_x = self.previous.width - self.current.width
        if self.previous.width > self.current.width:
            self.offset_x = -self.offset_x
        self.offset_y = self.previous.height - self.current.height
        if self.previous.height > self.current.height:
            _ = -self.offset_y

    def collect_garbage(self):
        del RESOLUTIONS[:]
        gc.collect()
        print("Garbage collected")
