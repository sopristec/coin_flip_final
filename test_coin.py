from coin import Coin
from player import Player

def test_coin_get_random_option():
    """Test that the coin option is set correctly"""
    coin = Coin()
    assert coin.get_random_option() in coin.options
    heads_count = 0
    tails_count = 0
    for _ in range(100):
        if coin.get_random_option() == 'HEADS':
            heads_count += 1
        if coin.get_random_option() == 'TAILS':
            tails_count += 1
    assert heads_count > 0
    assert tails_count > 0