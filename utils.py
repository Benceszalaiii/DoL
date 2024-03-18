import tkinter


def screen_size() -> dict[str, int]:
    """
    Get the current screen's dimensions
    
    Returns:
        dict(str, int)
        ["width"] -> width of screen
        ["height"] -> height of screen
    
    """
    root = tkinter.Tk()
    result = {
        "width": root.winfo_screenwidth(),
        "height": root.winfo_screenheight()
    }
    return result
    
    