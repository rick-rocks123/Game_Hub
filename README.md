# Game_Hub

A Python package that lets you play multiple games from the command line or directly in Python, including:

- Tic Tac Toe
- Rock Paper Scissors
- Guess the Number

---

## Installation

### ✅ pip (recommended)

```bash
py -m pip install Hub-Games
```
### ✅ pipx (best for CLI usage)

```bash
py -m pipx install Hub-Games
```
### ✅ uv (if you use uv package manager)

```bash
py -m uv pip install Hub-Games
```

### ✅ Development (editable install)

For testing or contributing:

```bash
git clone https://github.com/rick-rocks123/Game_Hub.git
cd <repo-folder>
pip install -e .
```

---

## Usage

### ✅ Command-line usage

Run a specific game using the CLI:

1️⃣Tic Tac Toe (pick starting player)

```bash
gamehub -t x # decided whether player x or o starts
```
2️⃣Rock Paper Scissors

```bash
gamehub -r
```
3️⃣ Guess the Number

```bash
gamehub -n 
```

### ✅ Bash commands

## Disclaimer: you can use -h or --help

```bash
gamehub --help
```

or

```bash
py gamehub --help
```


### ✅ Python usage
## Example 1: direct usage

```python
from gamehub import play_tic_tac_toe, play_rps, guess_number

games = {
    "tic_tac_toe": play_tic_tac_toe,
    "rps": play_rps,
    "number": guess_number
}

game_name = input("Which game? tic_tac_toe, rps, or number: ").strip()

if game_name in games:
    games[game_name]()  # ✅ call the function
else:
    print("Invalid game name")
```
## Example 2: usage with CLI-style arguments

```python
from gamehub import argparse_commands

def main():
    argparse_commands()

if __name__ == "__main__":
    main()
```
#### use -h or -help to see what cli-style arguments you have

---

## Game Gallery (ASCII Preview)

### Tic Tac Toe
    -----------
    |X | O | X|
    |O | X | O|
    |X | X | O|
    -----------
### Rock Paper Scissors (2 Players)

    Player one: rock
    Player two: scissors
    Player 1 wins!
    Score → P1: 1 | P2: 0

### Guess the Number

    Hello, Alice! I am thinking of a number between 1 and 10:
    input your guess: 5
    Too low!
    input your guess: 8
    Too high!
    input your guess: 7
    Alice guessed correctly in 3 guesses!



---

## Notes

- All games handle **graceful exits** if you press Ctrl+C or EOF.  
- Tic Tac Toe and RPS support 2-player CLI input.  
- Number Guessing randomly selects a number from 1–100.  
- You can add more games by following the `argparse_commands()` pattern.