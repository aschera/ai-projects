def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]

    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check for queens in the lower diagonal
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens_util(board, row, N, count):
    # Base case: All queens are placed
    if row == N:
        count[0] += 1
        print_solution(board, N, count[0])
        return

    # Try placing the queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 1

            # Recur to place the remaining queens in the next row
            solve_n_queens_util(board, row + 1, N, count)

            # Backtrack and remove the queen
            board[row][col] = 0


def print_solution(board, N, count):
    print(f"Solution {count}:")
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()
    print()


def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    count = [0]  # To keep track of the number of solutions

    solve_n_queens_util(board, 0, N, count)

    if count[0] == 0:
        print(f"No solution exists for {N}-Queens.")
    else:
        print(f"Total solutions for {N}-Queens: {count[0]}")


# Example usage:
N = 4
solve_n_queens(N)
