class Scene:
    def __init__(self, name: str, function: callable, *args):
        """
        Create a new Scene object. Can be later used with SceneManager

        Args:
            name (str): The name of the scene
            function: The function containing the code to the function
        """
        self.name = name
        self.function = function
        self.args = args

    def run(self):
        """
        Run the functions (Do not use youself. This is ment for SceneManager)
        """
        self.function(*self.args)

    def change_function(self, function):
        """
        Change the function of the scene

        Args:
            function : The function containing the code to the scene
        """
        self.function = function
