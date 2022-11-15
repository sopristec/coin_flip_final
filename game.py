"""Game class helps determine winners after every round and the definitive winner after 10 rounds"""

from typing import List

from player import Player
from coin import Coin

class Game:
    """Helps determine winners after every round and the definitive winner after 10 rounds"""

    def __init__(self, players: List[Player], coin: Coin):
        self.players = players
        self.coin = coin

    def print_the_winner(self, win_option: str) -> str:
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

    def print_definitive_winner(self) -> str:
        """Prints the definitive winner of the game"""

        print('FINAL SCORE')
        print(f'{self.players[0].get_name()}: {self.players[0].get_points()}')
        print(f'{self.players[1].get_name()}: {self.players[1].get_points()}')

        winner = None
        if self.players[0].get_points() > self.players[1].get_points():
            winner = self.players[0]
        else:
            winner = self.players[1]

        winning_message = f'The definitive winner is {winner.get_name()}'
        return winning_message
