
from game import Game
from player import Player
from coin import Coin

def test_game_print_the_winner_of_the_round():
    """Test that the winner is printed correctly"""
    player1 = Player('Player 1')
    player2 = Player('Player 2')
    player1.set_coin_option('HEADS')
    player2.set_coin_option('TAILS')
    players_list = [player1, player2]
    coin = Coin()
    game = Game(players_list, coin)
    winner_message = game.print_the_winner('HEADS')
    assert winner_message == 'Player 1 wins the round'
    winner_message = game.print_the_winner('TAILS')
    assert winner_message == 'Player 2 wins the round'

def test_game_print_offer_next_round():
    """Test that the offer to play next round is printed correctly"""
    player1 = Player('Player 1')
    player2 = Player('Player 2')
    players_list = [player1, player2]
    coin = Coin()
    game = Game(players_list, coin)
    offer_message = game.print_offer_next_round()
    assert offer_message == 'Press enter when ready for the next round.'

def test_game_print_definitive_winner():
    """Test that the definitive winner is printed correctly"""
    player1 = Player('Player 1')
    player2 = Player('Player 2')
    player1.add_points(1)
    player2.add_points(2)
    players_list = [player1, player2]
    coin = Coin()
    game = Game(players_list, coin)
    winner_message = game.print_definitive_winner_message()
    assert winner_message == 'The definitive winner is Player 2'