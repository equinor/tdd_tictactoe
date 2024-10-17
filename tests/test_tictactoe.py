import unittest
from src.tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_board_initialization(self):
        game = TicTacToe()
        expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(game.board, expected_board, "The board should initialize as a 3x3 grid of empty strings")
        print("test_board:initialization passed")
        
        
        
    def test_player_switch(self):
        game = TicTacToe()
        self.assertEqual(game.current_player, "X", "The starting player should be X")
        game.switch_player()
        self.assertEqual(game.current_player, "O", "After switching, the current player should be O")
        game.switch_player()
        self.assertEqual(game.current_player, "X", "After switching again, the current player should be X")
        print("test_player_switch passed")
        
        
    def test_make_move(self):
        game = TicTacToe()
        self.assertEqual(game.make_move(0, 0), True, "The first move should be valid")
        self.assertEqual(game.make_move(0, 0), False, "The same move should be invalid")
        self.assertEqual(game.make_move(0, 1), True, "A different move should be valid")
        self.assertEqual(game.make_move(0, 1), False, "The same move should be invalid")
        print("test_make_move passed")
        
        
    def test_check_winner(self):
        game = TicTacToe()
        self.assertEqual(game.check_winner(), None, "There should be no winner at the start of the game")
        game.make_move(0, 0)
        game.make_move(1, 0)
        game.make_move(0, 1)
        game.make_move(1, 1)
        game.make_move(0, 2)
        self.assertEqual(game.check_winner(), "X", "X should win with a top row")
        print("test_check_winner passed")

if __name__ == '__main__':
    unittest.main()
