import unittest
from src.tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_board_initialization(self):
        game = TicTacToe()
        expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(game.board, expected_board, "The board should initialize as a 3x3 grid of empty strings")
        print("test_board:initialization passed")

if __name__ == '__main__':
    unittest.main()
