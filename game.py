"""Game class helps determine winners after every round and the definitive winner after 10 rounds"""

from typing import List

from player import Player
from coin import Coin

class Game:
    """Helps determine winners after every round and the definitive winner after 10 rounds"""

    def __init__(self, players: List[Player], coin: Coin):
        """Initializes the game with the players and the coin.
        ATTENTION. The game class expects a list of exactly 2 players."""
        # TODO: Add a check to make sure the list has exactly 2 different players
        self.players = players
        self.coin = coin

    def print_the_round_winner(self, win_option: str) -> str:
        """Prints the winner and loser of the round"""

        winner = None
        if self.players[0].did_player_win(win_option):
            winner = self.players[0]
        else:
            winner = self.players[1]

        winning_message = f'{winner.get_name()} wins the round'
        print(winning_message)
        winner.add_points(1)
        return winning_message

    def print_offer_next_round(self) -> str:
        """Prints the offer to play another round"""
        message = 'Press enter when ready for the next round.'
        print(message)
        return message

    def print_definitive_winner_message(self) -> str:
        """Prints the definitive winner of the game"""

        print('FINAL SCORE')
        print(f'{self.players[0].get_name()}: {self.players[0].get_points()}')
        print(f'{self.players[1].get_name()}: {self.players[1].get_points()}')

        winning_message = ''
        if self.players[0].get_points() > self.players[1].get_points():
            winning_message = f'The definitive winner is {self.players[0].get_name()}'
        if self.players[0].get_points() < self.players[1].get_points():
            winning_message = f'The definitive winner is {self.players[1].get_name()}'
        if self.players[0].get_points() == self.players[1].get_points():
            winning_message = 'Match tied! Keep playing c:'

        return winning_message
