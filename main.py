import copy
from math import floor

ttt = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

victor = 0
playing = True
turn = 0
gofirst = False


def check_win(board):
    value = 0

    # row
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            value = board[i][0]

    # column
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            value = board[0][i]

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        value = board[0][0]

    if board[2][0] == board[1][1] == board[0][2] != 0:
        value = board[2][0]

    return value


def actions(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                moves.append([i, j])
    return moves


def result(row, col, board, player):
    new_board = copy.deepcopy(board)
    new_board[row][col] = player
    return new_board


def is_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True


# I've never hated coding so much
def minimax(board, player):
    if check_win(board) != 0:
        if check_win(board) == 1:
            return 1, None
        else:
            return -1, None
    elif is_complete(board):
        return 0, None

    if player == 1:
        best_value = float('-inf')
        for col, row in actions(board):
            new_board = result(col, row, board, player)
            value, _ = minimax(new_board, -1)
            if value > best_value:
                best_value = value
                best_move = [col, row]
    else:
        best_value = float('inf')
        for col, row in actions(board):
            new_board = result(col, row, board, player)
            value, _ = minimax(new_board, 1)
            if value < best_value:
                best_value = value
                best_move = [col, row]

    return best_value, best_move


def user_move():
    valid_move = False
    while not valid_move:
        move = int(input("Enter your move (1-9): "))
        row = floor(move/3 - .1)
        col = move % 3 - 1
        if ttt[row][col] == 0:
            ttt[row][col] = -1
            valid_move = True
        else:
            print("Invalid move. Try again.")


def print_board():
    xos = []
    num2xo = {
        -1: "x",
        1: "o",
        0: " "
    }
    for i in range(3):
        for j in range(3):
            xos.append(num2xo[ttt[i][j]])

    print(xos[0] + '|' + xos[1] + '|' + xos[2])
    print('-----')
    print(xos[3] + '|' + xos[4] + '|' + xos[5])
    print('-----')
    print(xos[6] + '|' + xos[7] + '|' + xos[8])


stillPlaying = True

while stillPlaying:
    print_board()
    while playing:
        if turn % 2 == 0:
            print("Your move")
            user_move()
        else:
            print("Bot move")
            bot_move = minimax(copy.deepcopy(ttt), 1)
            ttt[bot_move[1][0]][bot_move[1][1]] = 1

        turn += 1

        victor = check_win(ttt)
        if victor != 0:
            playing = False
        if is_complete(ttt):
            playing = False

        print_board()

    if victor == -1:
        print("You win")
    elif victor == 1:
        print("Bot wins")
    else:
        print("Draw")

    if input("Play again? (yes/no): ") == "yes":
        if gofirst:
            turn = 0
        else:
            turn = 1
        ttt = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        victor = 0
        gofirst = not gofirst
        playing = True
    else:
        stillPlaying = False
