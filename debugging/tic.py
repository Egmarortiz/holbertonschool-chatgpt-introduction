#!/usr/bin/python3
def print_board(board):
    """
    Print the 3×3 board, with separators between (but not after) rows.
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_winner(board):
    """
    Check for three-in-a-row in rows, columns, or diagonals.
    Returns True if there's a winner.
    """
    # Rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return True
    # Columns
    for col in range(3):
        if (board[0][col] != " " and
            board[0][col] == board[1][col] == board[2][col]):
            return True
    # Diagonals
    if (board[0][0] != " " and
        board[0][0] == board[1][1] == board[2][2]):
        return True
    if (board[0][2] != " " and
        board[0][2] == board[1][1] == board[2][0]):
        return True
    return False


def tic_tac_toe():
    """
    Main game loop. Players alternate placing X/O until someone wins
    or the board is full (draw).
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    moves = 0

    while True:
        print_board(board)
        # Input with validation
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter col (0-2): "))
        except ValueError:
            print("Invalid input; please enter numbers 0, 1, or 2.")
            continue
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Coordinates out of range; try again.")
            continue
        if board[row][col] != " ":
            print("That spot is taken; try again.")
            continue

        # Place mark
        board[row][col] = player
        moves += 1

        # Check for win
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check for draw
        if moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()

