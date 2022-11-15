"""Module containing the Coin class."""

import random

class Coin:
    """Holds every Coin class instance state and selects a random option"""

    options = ('HEADS', 'TAILS')
    selected_option = None

    def get_random_option(self) -> str:
        """Selects a random option from the options list"""

        self.selected_option = random.choice(self.options)
        return self.selected_option
