def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == abs(i-row):
            return False
    return True

def solve_n_queens(row, board, n):
    if row == n:
        print(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(row + 1, board, n)

n = int(input("Enter size of the board (N): "))
solve_n_queens(0, [0]*n, n)