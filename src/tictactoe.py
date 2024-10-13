class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('---------')

    def make_move(self, row, col, player):
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError("Move is out of bounds")
        if self.board[row][col] != ' ':
            raise ValueError("Invalid move! Cell is already occupied.")
        self.board[row][col] = player

    def check_winner(self, player):
        board = self.board
        # Check horizontal, vertical, and diagonal lines for a win
        for i in range(3):
            if all(cell == player for cell in board[i]) or \
               all(board[j][i] == player for j in range(3)):
                return True
        if board[0][0] == board[1][1] == board[2][2] == player or \
           board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    def check_tie(self):
        return all(cell in ['X', 'O'] for row in self.board for cell in row) and not self.check_winner('X') and not self.check_winner('O')

    def is_valid_move(self, row, col):
        return 0 <= row <= 2 and 0 <= col <= 2 and self.board[row][col] == ' '

    def play_game(self):
        current_player = 'X'
        while True:
            self.print_board()
            try:
                row = int(input(f"Player {current_player}, enter row number (1-3): ")) - 1
                col = int(input(f"Player {current_player}, enter column number (1-3): ")) - 1
                if self.is_valid_move(row, col):
                    self.make_move(row, col, current_player)
                else:
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
            except IndexError:
                print("Row and column numbers must be 1, 2, or 3.")
                continue

            if self.check_winner(current_player):
                self.print_board()
                print(f"Player {current_player} wins!")
                break
            elif self.check_tie():
                self.print_board()
                print("It's a tie!")
                break

            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
