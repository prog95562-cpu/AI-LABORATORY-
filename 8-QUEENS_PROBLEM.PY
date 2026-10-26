# Experiment 7: 8 Queens Problem Using Backtracking

N = 8


def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))


def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True


def solve_queens(board, row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_queens(board, row + 1):
                return True

            board[row][col] = 0

    return False


board = [[0 for _ in range(N)] for _ in range(N)]

if solve_queens(board, 0):
    print("Solution for 8 Queens Problem:")
    print_solution(board)
else:
    print("No solution exists.")