def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_q(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, n):
    if row == n:
        print_board(board)
        return True

    found = False
    for col in range(n):
        if check_q(board, row, col, n):
            board[row][col] = 'Q'
            found = solve(board, row + 1, n) or found
            board[row][col] = '.'

    return found

n = int(input("Enter value of N: "))
board = [['.' for _ in range(n)] for _ in range(n)]

if not solve(board, 0, n):
    print("No solution exists")
