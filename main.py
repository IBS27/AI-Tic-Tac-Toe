# Tic Tac Toe game in python

board = [" " for x in range(10)]  # 10 and not 9 because user input between 1-9


def insert_letter(letter, pos):
    board[pos] = letter


def space_is_free(pos):
    return board[pos] == " "


def print_board(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")


def is_winner(bo, le):
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le)  # Horizontal rows
        or (bo[4] == le and bo[5] == le and bo[6] == le)
        or (bo[1] == le and bo[2] == le and bo[3] == le)
        or (bo[1] == le and bo[4] == le and bo[7] == le)  # Vertical columns
        or (bo[2] == le and bo[5] == le and bo[8] == le)
        or (bo[3] == le and bo[6] == le and bo[9] == le)
        or (bo[1] == le and bo[5] == le and bo[9] == le)  # Diagonals
        or (bo[3] == le and bo[5] == le and bo[7] == le)
    )


def player_move():
    run = True
    while run:
        # Getting player input
        move = input("Please selet a position to place an 'X', (1-9): ")

        # Evaluating whether the player gave a valid input
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter("X", move)
                else:
                    print("Sorry, this space is occupied!")
            else:
                print("Please type a number within the range!")
        except ValueError:
            print("Please type a number!")


def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    # Checking for a winning move
    for let in ["O", "X"]:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    # Checking if corners are free
    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    # Checking if center is free
    if 5 in possible_moves:
        move = 5
        return move

    # Checking if edges are free
    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move


def select_random(li):  # Selecting random move
    import random

    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def is_board_full(board):  # Checking if the board is full
    if board.count(" ") > 1:
        return False
    else:
        return True


# Main Game Loop
def main():
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not is_board_full(board):
        if not is_winner(board, "O"):  # Checking if computer won
            player_move()
            print_board(board)
        else:
            print("Sorry, O's won this time!")
            break

        if not is_winner(board, "X"):  # Checking if player won
            move = comp_move()
            if move == 0:
                print("Tie Game!")
            else:
                insert_letter("O", move)
                print("Computer placed an 'O' in position", move, ":")
                print_board(board)
        else:
            print("X's won this time! Good job!")
            break


main()
