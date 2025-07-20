# Random Number Guessing Game

This is a simple command-line game built in Python. The program randomly selects a number between 1 and 100 and prompts the user to guess it. It provides hints along the way and tracks the number of attempts.

## Technologies

- Python (standard library)
- random
- functions

## Features

- Custom hint logic: "higher" or "lower" after each guess
- Extra hints after 2 incorrect tries (e.g., even/odd, multiple of 5)
- Input validation to ensure clean user experience
- Replay functionality at the end of each game
- Modular design using Python functions

## How to Play

```bash
python guessing_game.py
```

Follow the prompts and try to guess the number with the fewest attempts possible!

## Files

```
guessing-game/
│
├── guessing_game.py      # Main game file
└── README.md             # Overview and instructions
```

## Example Hint Logic

- "Try a higher number!"
- "The number is even and a multiple of 5"
- "Correct! You guessed it in 7 tries."

## License

MIT License
