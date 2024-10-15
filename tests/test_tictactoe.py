import unittest
from src.tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_board_initialization(self):
        game = TicTacToe()
        expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(game.board, expected_board, "The board should initialize as a 3x3 grid of empty strings")
        print("test_board:initialization passed")

    def test_make_move(self):
        game = TicTacToe()
        game.make_move(0, 0, 'X')
        self.assertEqual(game.board[0][0], 'X', "The first move should place an 'X' in the top-left corner of the board")
        print("test_make_move passed")

    def test_check_winner_horizontal(self):
        game = TicTacToe()
        game.board = [['X', 'X', 'X'], ['', '', ''], ['', '', '']]
        self.assertTrue(game.check_winner('X'), "Player X should be the winner with a horizontal line")
        print("test_check_winner_horizontal passed")

    def test_check_winner_vertical(self):
        game = TicTacToe()
        game.board = [['X', '', ''], ['X', '', ''], ['X', '', '']]
        self.assertTrue(game.check_winner('X'), "Player X should be the winner with a vertical line")
        print("test_check_winner_vertical passed")

    def test_check_winner_diagonal(self):
        game = TicTacToe()
        game.board = [['X', '', ''], ['', 'X', ''], ['', '', 'X']]
        self.assertTrue(game.check_winner('X'), "Player X should be the winner with a diagonal line")
        print("test_check_winner_diagonal passed")

    def test_check_tie(self):
        game = TicTacToe()
        game.board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
        self.assertTrue(game.check_tie(), "The game should be a tie when all fields are filled and there's no winner")
        print("test_check_tie passed")

    def test_valid_move(self):
        game = TicTacToe()
        try:
            game.make_move(2, 2, 'X')  # Middle of the board should be a valid move
        except ValueError:
            self.fail("make_move() raised ValueError unexpectedly for a valid move!")

    def test_invalid_move_out_of_bounds(self):
        game = TicTacToe()
        with self.assertRaises(ValueError):
            game.make_move(3, 4, 'X')  # Outside the board should raise ValueError

    def test_invalid_move_to_occupied_cell(self):
        game = TicTacToe()
        game.make_move(1, 1, 'X')  # Make an initial valid move
        with self.assertRaises(ValueError):
            game.make_move(1, 1, 'O')  # Attempting to move to the same cell should raise ValueError

if __name__ == '__main__':
    unittest.main()
