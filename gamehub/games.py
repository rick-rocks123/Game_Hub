import random
import sys
import argparse


# ---------- SAFE INPUT ----------
def safe_input(prompt):
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None  # signals caller to stop the current game gracefully

# ---------- ROCK PAPER SCISSORS ----------
def play_rps():
    """Start a best-of-3 Rock Paper Scissors game."""
    print("welcome to rock paper scissors")

    player_one = 0
    player_two = 0

    while player_one < 3 and player_two < 3:
        P1 = safe_input("Player one, rock(r), paper(p), or scissors(s): ")
        if P1 is None:
            return  # EOF → stop this game
        P2 = safe_input("Player two, rock(r), paper(p), or scissors(s): ")
        if P2 is None:
            return

        P1 = P1.lower().strip()
        P2 = P2.lower().strip()

        player_one, player_two = conditions(P1, P2, player_one, player_two)

        print(f"Score → P1: {player_one} | P2: {player_two}\n")


def conditions(P1, P2, player_one, player_two):
    wins = {
        ("rock", "scissors"),
        ("scissors", "paper"),
        ("paper", "rock"),
        ("r", "s"),
        ("s", "p"),
        ("p", "r")
    }
    if P1 == P2:
        print("tie")

    elif (P1, P2) in wins:
        print("player 1 wins")
        player_one += 1

    elif (P2, P1) in wins:
        print("player 2 wins")
        player_two += 1

    else:
        print("invalid input, please try again")

    return player_one, player_two


# ---------- TIC TAC TOE ----------
def play_tic_tac_toe():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    player = "x"
    total = 0

    while total < 9:
        print(f"player: {player} go")

        row, col = user_input(board)
        if row is None:
            return  # EOF → stop this game

        board[row][col] = player
        print_board(board)
        total += 1

        if has_three_in_a_row(board):
            print(f"player {player} wins")
            break

        player = "o" if player == "x" else "x"


def has_three_in_a_row(board):
    # rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != " ":
            return True

    # columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != " ":
            return True

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def print_board(board):
    for row in range(3):
        print(f" {board[row][0]} | {board[row][1]} | {board[row][2]} ")
        if row < 2:
            print("-----------")


def user_input(board):
    while True:
        r = safe_input("row 0-2: ")
        if r is None:
            return None, None  # EOF → stop this game
        c = safe_input("col 0-2: ")
        if c is None:
            return None, None

        try:
            row = int(r)
            col = int(c)
            if board[row][col] != " ":
                print("spot taken, try again")
                continue
            return row, col
        except (IndexError, ValueError):
            print("input valid int not a str and range 0-2")


# ---------- GUESS THE NUMBER ----------
def guess_number():
    number = random.randint(1, 10)

    player_name = safe_input("Hello, What's your name? ")
    if player_name is None:
        return  # EOF → stop this game

    number_of_guesses = 0

    print("Okay, " + player_name + "! I am guessing a number between 1 and 10:")

    while True:
        g = safe_input("input your guess: ")
        if g is None:
            return  # EOF → stop this game

        try:
            guess = int(g)
            number_of_guesses += 1
            if guess > number:
                print("your guess is too high")
            elif guess < number:
                print("your guess is too low")
            else:
                print(f"{player_name} guessed correctly in {number_of_guesses} guesses")
                break
        except ValueError:
            print("Please enter a valid integer.")

def argparse_commands():

    parser = argparse.ArgumentParser(
        prog='GameHub',
        description='Multiple games: Tic Tac Toe Game, RPS, Number Guessing',
        epilog='unknown games will result in an end to the function'
    )

    parser.add_argument(
        "-t", "--tic_tac_toe", choices=['X', 'O', 'x', 'o'],
        type=str, help="pick which player starts x or o"
    )

    parser.add_argument("-r", "--rps", action="store_true")
    parser.add_argument("-n", "--number", action="store_true")

    args = parser.parse_args()

    game_dict = {
        "tic_tac_toe": play_tic_tac_toe,
        "rps": play_rps,
        "number": guess_number
    }

    any_game_run = False
    for game_name, game in game_dict.items():
        if getattr(args, game_name):
            game()
            any_game_run = True

    if not any_game_run:
        print("No game selected. Use -t, -r, or -n to play a game.")
        sys.exit()
