from shimoku_api_python import Client
from utils.utils import get_data


class Board:
    """
    A class used to represent a Dashboard for displaying various data visualizations.

    Attributes:
        board_name (str): Name of the dashboard.
        dfs (DFs): An instance of a DFs class for handling data frames.
        shimoku (Client): An instance of a Client class for Shimoku API interactions.
    """

    def __init__(self, shimoku: Client):
        """
        The constructor for the Dashboard class.

        Parameters:
            shimoku (Client): An instance of a Client class for Shimoku API interactions.
        """

        self.board_name = "Reporte de ingresos"  # Name of the dashboard
        self.dfs1 = get_data("data/productos.csv")
        self.dfs2 = get_data("data/ventas.csv")
        self.shimoku = shimoku  # Shimoku client instance
        self.shimoku.set_board(name=self.board_name)  # Setting up the board in Shimoku

    def plot(self):
        """
        A method to plot user overview.

        This method utilizes the UserOverview class from the paths.user_overview
        module to create and display a plot related to the user. It assumes that
        UserOverview requires a reference to the instance of the class from which
        this method is called.

        Args:
        self: A reference to the current instance of the class.

        Returns:
        None. The function is used for its side effect of plotting data.

        Note:
        - This method imports the UserOverview class within the function scope
          to avoid potential circular dependencies.
        - Ensure that the UserOverview class has access to all necessary data
          through the passed instance.
        """

        from paths.user_overview import UserOverview

        UO = UserOverview(self)
        UO.plot()
