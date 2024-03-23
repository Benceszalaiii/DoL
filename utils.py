# ----------- #
#   IMPORTS   #
# ----------- #
import tkinter
from settings import RESOLUTIONS

# ----------- #
#  FUNCTIONS  #
# ----------- #
class Screen:
    def __init__(self):
        self.width: int = 0
        self.height: int = 0
        self.screen_size()
    
    # Get active screen's resolution
    def screen_size(self) -> None:
        """
        Get the current screen's dimensions
        """
        root = tkinter.Tk()

        self.width = int(root.winfo_screenwidth())
        self.height = int(root.winfo_screenheight())


def resolution_parse(resolution: str | tuple[int]) -> tuple[int] | str:
    """
        Returns a resolution string as tuple(width: int, height: int)
        or returns a tuple(width: int, height: int) as a string 
        
        For example: 
        (1600, 900) -> "1600x900"
        "1600x900"  -> (1600, 900)
    """
    if type(resolution) is str:
        try:
            result = resolution.split("x")
        except ValueError:
            print("Values incorrect")
            return "error"
        try:
            result = tuple(map(int, result))
        except:
            print("Values can not be formatted as integers")
            
        if len(result) == 2:
            print("Parse successful")
            return result
        else:
            print("More/Less than expected arguments")
    else:
        if len(screen_size) == 2:
            try:
                width, height = screen_size[0], screen_size[1]
            except:
                print("Something unexpected happened while parsing int to str")
                return "error"
            try:
                return str(width) + "x" + str(height)
            except:
                print("Cannot return parsed string")
                return "error"
        else:
            print("More/Less arguments than expected")
            return "error"

print(type(RESOLUTIONS))
print(RESOLUTIONS)
def available_resolutions():
    global RESOLUTIONS
    screen_size = Screen()
    available = [(screen_size.width, screen_size.height)]
    for res in RESOLUTIONS:
        print(type(res))
        print(type(screen_size.width))
        if not res[0] > screen_size.width or not res[1] > screen_size.height and not res in available:
            available.append(res)
    RESOLUTIONS = available
available_resolutions()
print(RESOLUTIONS)