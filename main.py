import argparse
from os import getenv
from shimoku_api_python import Client
#from dotenv import load_dotenv

from board import Board


def main():
    """
    Main function to initialize and plot the dashboard.

    This script initializes a Shimoku client, deletes existing boards and menu paths,
    and then creates and plots a new dashboard.
    """
    # Load environment variables
    access_token = '7b1dbf01-08a7-4ab0-9162-a3df6968487b'
    universe_id: str = 'dfc83c69-7770-42e9-a052-a60f95a1c44e'
    workspace_id: str = 'f017979c-1cb5-438e-b83c-a09264b4d88a'

    # Create the Shimoku client with necessary credentials
    shimoku = Client(
        access_token=access_token,
        universe_id=universe_id,
        verbosity="INFO"
    )
    shimoku.set_workspace(uuid=workspace_id)
    #shimoku.set_workspace()

    # Delete all existing boards and menu paths in the workspace
    shimoku.workspaces.delete_all_workspace_menu_paths()
    shimoku.workspaces.delete_all_workspace_boards()

    # Instantiate and set up the dashboard
    board = Board(shimoku)
    board.plot()  # Plot the dashboard


if __name__ == "__main__":
    main()
