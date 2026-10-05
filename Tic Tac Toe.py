# Tic Tac Toe Game
# Two Player Console Game

board = [" " for _ in range(9)]


def display_board():
    print()
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("-----|-----|-----")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("-----|-----|-----")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True

    return False


def check_draw():
    return " " not in board


def play_game():
    current_player = "X"

    print("================================")
    print("       TIC TAC TOE GAME")
    print("================================")

    print("\nPosition numbers:")
    print("  1  |  2  |  3")
    print("-----|-----|-----")
    print("  4  |  5  |  6")
    print("-----|-----|-----")
    print("  7  |  8  |  9")

    while True:
        display_board()

        print(f"Player {current_player}'s turn")

        try:
            position = int(input("Enter position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            index = position - 1

            if board[index] != " ":
                print("That position is already occupied!")
                continue

            board[index] = current_player

            if check_winner(current_player):
                display_board()
                print(f"🎉 Player {current_player} wins!")
                break

            if check_draw():
                display_board()
                print("🤝 It's a draw!")
                break

            # Change player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        except ValueError:
            print("Invalid input! Please enter a number.")


# Start the game
play_game()