import sys
from gamehub import play_rps, play_tic_tac_toe, guess_number, safe_input

def main():
    while True:
        print("Welcome to GameHub")
        print("1 - Rock Paper Scissors")
        print("2 - Tic Tac Toe")
        print("3 - Guess The Number")

        choice = safe_input("Choose a game (1-3) or quit: ")

        # 👇 handle EOF / CTRL+C safely
        if choice is None:
            print("\nGoodbye 👋")
            sys.exit()

        choice = choice.lower().strip()

        games = {
            "1": play_rps,
            "2": play_tic_tac_toe,
            "3": guess_number
        }

        if choice in games:
            games[choice]()

        elif choice in ("quit", "q"):
            break
        else:
            print("Invalid choice\n")
    print("Goodbye 👋")

if __name__ == "__main__":
    main()