#!/usr/bin/env python
"""The main Coin Flip Game module orchestrates the interaction among all modules."""

import random
import time

from game import Game
from coin import Coin
from player import Player

def main(default_wait_between_rounds = 3) -> str:
    """The main function simply makes the whole game work."""

    player_1_name = input('What is Player 1\'s name?')
    player_2_name = input('What is Player 2\'s name?')

    player1 = Player(player_1_name)
    player2 = Player(player_2_name)
    players_list = [player1, player2]
    coin = Coin()
    game = Game(players_list, coin)

    # First player is a random player selected by the machine at the beginning of the game
    first_player = random.choice(players_list)
    for player in players_list:
        if player.get_name() != first_player.get_name():
            second_player = player

    rounds = 1
    second_player_option = None

    while rounds <= 10:

        print(f'ROUND {rounds}')
        print(f'{first_player.get_name()} has been selected to flip the coin')
        first_player_option = ""
        while first_player_option.upper() != 'H' and first_player_option.upper() != 'T':
            first_player_option = input(
                f'{first_player.get_name()} pick an option [H]EADS or [T]AILS: ')

        if first_player_option == 'H':
            first_player.set_coin_option('HEADS')
            second_player.set_coin_option('TAILS')
            second_player_option = 'TAILS'
        else:
            first_player.set_coin_option('TAILS')
            second_player.set_coin_option('HEADS')
            second_player_option = 'HEADS'

        print(f'{second_player.get_name()} will be {second_player_option}')
        print('Coin is in the air...')
        time.sleep(default_wait_between_rounds)

        win_option = coin.get_random_option()

        print(f'Result is {win_option} ')

        game.print_the_round_winner(win_option)
        game.print_offer_next_round()

        rounds += 1

    return game.print_definitive_winner_message()

if __name__ == '__main__':
    main()
