def display_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")


def player_input(board, player):
    while True:
        try:
            move = int(
                input(f"Player {player}, enter a available position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number from 1 to 9.")


def check_win(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


def check_draw(board):
    return ' ' not in board


def switch_player(current_player):
    return 'O' if current_player == 'X' else 'X'


def play_game():
    board = [' '] * 9
    current_player = 'X'
    display_board(board)

    while True:
        player_input(board, current_player)
        display_board(board)

        if check_win(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        current_player = switch_player(current_player)


# Run the game
play_game()
