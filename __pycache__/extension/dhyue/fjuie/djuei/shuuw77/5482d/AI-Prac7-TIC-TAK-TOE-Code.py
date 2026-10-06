def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    print("TIC-TAC-TOE")
    print("Player X and Player O")

    while True:
        print_board(board)

        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))

        if board[row][col] != ' ':
            print("Position already occupied!")
            continue

        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print("Player", player, "wins!")
            break

        if check_draw(board):
            print_board(board)
            print("Game Draw!")
            break

        if player == 'X':
            player = 'O'
        else:
            player = 'X'


tic_tac_toe()
