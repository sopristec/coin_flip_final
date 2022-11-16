"""Test the whole Coin Flip game"""

import unittest
from unittest.mock import patch
import coin_flip

class CoinFlipTest(unittest.TestCase):
    """Test the whole Coin Flip game"""

    def setUp(self):
        pass

    @patch('builtins.input')
    def test_coin_flip_main(self, mock_input):
        """Test that the coin flip game, after 10 rounds given the same inputs,
        will produce at least one win for Player 1 and one win for Player2."""
        one_round_inputs = [
            'Player 1', 'Player 2', 'H', 'T', 'H', 'T', 'H', 'T', 'H', 'T', 'H', 'T',]
        rounds_count = 10
        inputs = []
        for _ in range(rounds_count):
            inputs.extend(one_round_inputs)
        mock_input.side_effect = inputs
        results = []
        for _ in range(rounds_count):
            definitive_winner_message = coin_flip.main(0.01)
            results.append(definitive_winner_message)
        self.assertIn('The definitive winner is Player 1', results)
        self.assertIn('The definitive winner is Player 2', results)

if __name__ == '__main__':
    unittest.main()
