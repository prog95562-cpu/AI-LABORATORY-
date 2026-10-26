# Experiment 9: Tic-Tac-Toe Using Minimax Algorithm

def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print()


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_moves_left(board):
    return any(" " in row for row in board)


def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 10 - depth

    if check_winner(board, "X"):
        return depth - 10

    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = float("-inf")

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = " "

        return best

    best = float("inf")

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                best = min(best, minimax(board, depth + 1, True))
                board[i][j] = " "

    return best


def computer_move(board):
    best_score = float("-inf")
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    if move:
        board[move[0]][move[1]] = "O"


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Tic-Tac-Toe")
    print("You: X | Computer: O")
    print("Enter row and column from 1 to 3.")

    while True:
        print_board(board)

        try:
            row, col = map(
                int, input("Enter row and column: ").split()
            )
        except ValueError:
            print("Enter two numbers separated by a space.")
            continue

        row -= 1
        col -= 1

        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid position. Try again.")
            continue

        if board[row][col] != " ":
            print("Cell already occupied. Try again.")
            continue

        board[row][col] = "X"

        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            break

        if not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            break

        computer_move(board)

        if check_winner(board, "O"):
            print_board(board)
            print("Computer wins!")
            break

        if not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            break


play_game()