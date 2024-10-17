class TicTacToe:
    
    def __init__(self):
        self.current_player = "X"
              
        grid = 3
        board = []
        
        for i in range(grid):
            board.append([])
            for j in range(grid):
                board[i].append(" ")

        self.board = board
        
        
    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
        
        return self.current_player
    
    
    def make_move(self, row, col):
        row -= 1
        col -= 1
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.switch_player()
            return True
        else:
            return False
        
        
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]
        return None
    
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True
    
    
    def play_game(self):
        while self.check_winner() is None and not self.check_draw():
            
            for row in self.board:
                print(row)
            
            try:
                row = int(input("Enter the row (1-3): "))
                col = int(input("Enter the column (1-3): "))
                if row not in range(1, 4) or col not in range(1, 4):
                    print("Invalid input. Please enter a number between 1 and 3.")
                    continue
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if not self.make_move(row, col):
                print("Invalid move, cell is already taken.")
            
        winner = self.check_winner()
        if winner:
            print(f"{winner} wins!")
        else:
            print("It's a draw!")

if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
