from player import Player

def test_player_name():
    """Test that the player name is set correctly"""
    player = Player('Player 1')
    assert player.get_name() == 'Player 1'

def test_player_coin_option():
    """Test that the coin option is set correctly"""
    player = Player('Player 1')
    player.set_coin_option('HEADS')
    assert player.get_selected_coin_option() == 'HEADS'

def test_did_player_win():
    """Test that the player won"""
    player = Player('Player 1')
    player.set_coin_option('HEADS')
    assert player.did_player_win('HEADS') is True

def test_did_player_lose():
    """Test that the player lost"""
    player = Player('Player 1')
    player.set_coin_option('HEADS')
    assert player.did_player_win('TAILS') is False

def test_player_points():
    """Test that the player points are set correctly"""
    player = Player('Player 1')
    player.add_points(1)
    assert player.get_points() == 1
