"""Module containing the Player class."""

class Player:
    """Holds every Player class instance state."""

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.selected_coin_option = None

    def get_name(self) -> str:
        """Returns the player name"""
        return self.name

    def get_selected_coin_option(self) -> str:
        """Returns the player selected coin option"""
        return self.selected_coin_option

    def set_coin_option(self, coin_option: str) -> str:
        """Sets the player coin selection"""
        self.selected_coin_option = coin_option
        return self.selected_coin_option

    def did_player_win(self, winning_option: str) -> bool:
        """Returns True if the winning option is the same as the player selected option"""
        return self.selected_coin_option == winning_option

    def get_points(self) -> int:
        """Returns the player points"""
        return self.points

    def add_points(self, points_to_add: int) -> int:
        """Adds points to the player"""
        self.points+=points_to_add
        return self.points
