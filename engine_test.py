import unittest
from engine import GameEngine

class EngineTester(unittest.TestCase):
    def setUp(self):
        self.engine = GameEngine()

    def test_find_winner(self):
        """
        Setting up player moves and computer moves
        for simulate game then run func for finding winner
        and compare result
        """
        self.engine.player_moves = [3, 5, 7]
        self.engine.computer_moves = [1, 2, 4]
        self.engine.find_winner()
        self.assertEqual(self.engine.winner, "Player")

        self.engine.player_moves = [3, 5, 9]
        self.engine.computer_moves = [1, 7, 4]
        self.engine.find_winner()
        self.assertEqual(self.engine.winner, "Bot")

        self.engine.player_moves = [3, 5, 8, 9, 4]
        self.engine.computer_moves = [1, 2, 6, 7]
        self.engine.find_winner()
        self.assertEqual(self.engine.winner, "Tie")

    def test_choose_ai_move_hard(self):
        """
        Setting up player moves and computer moves
        for simulate game then run func for choosing ai's move
        and compare result
        """
        self.engine.player_moves = [3, 5, 9]
        self.engine.computer_moves = [1, 4]
        self.assertEqual(self.engine.choose_ai_move_hard(), 7)

    def test_choose_ai_move_easy(self):
        """
        Setting up player moves and computer moves
        for simulate game then run func for choosing ai's move
        and compare result
        """
        self.engine.player_moves = [3, 5, 9]
        self.engine.computer_moves = [1, 4]
        self.assertEqual(self.engine.choose_ai_move_easy(), 7)

if __name__ == '__main__':
    unittest.main()
