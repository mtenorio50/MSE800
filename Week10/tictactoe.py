class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def display_board(self):
        print("\n")
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("\n")

    def make_move(self):
        while True:
            try:
                pos = int(
                    input(f"Player {self.current_player}, choose (1–9): ")) - 1
                if 0 <= pos <= 8 and self.board[pos] == ' ':
                    self.board[pos] = self.current_player
                    break
                else:
                    print("Invalid. Try again.")
            except ValueError:
                print("Use a number 1-9.")

    def check_win(self):
        wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(self.board[a] == self.board[b] == self.board[c] == self.current_player for a, b, c in wins)

    def check_draw(self):
        return ' ' not in self.board

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        self.display_board()
        while True:
            self.make_move()
            self.display_board()
            if self.check_win():
                print(f"{self.current_player} wins!")
                break
            elif self.check_draw():
                print("It's a draw!")
                break
            self.switch_player()


# Run
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
