# Quiz Game

A small command-line quiz game written in Python.

## Requirements

- Python 3.8 or newer

## Start the Game with a Virtual Environment

### macOS/Linux

From the project folder, create the virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Start the game:

```bash
python main.py
```

When you finish playing, leave the virtual environment with:

```bash
deactivate
```

### Windows

From the project folder, create the virtual environment:

```powershell
py -m venv .venv
```

Activate it in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Start the game:

```powershell
python main.py
```

When you finish playing, leave the virtual environment with:

```powershell
deactivate
```

The game does not need any packages installed with `pip`; the virtual environment keeps its Python setup separate from the rest of your computer.

## Project Files

- `main.py` - Starts the game, asks for the player's name, runs the quiz, and displays the final score.
- `questions.py` - Stores the quiz questions, answer choices, and correct answers.
- `quiz.py` - Displays each question, checks the selected answer, and calculates the score.
- `utils.py` - Formats and displays the final score and feedback message.
- `Readme.md` - Explains how to set up and run the game.