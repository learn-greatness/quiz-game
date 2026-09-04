# Contributing to Quiz Game

Welcome! This project is a beginner-friendly place to practice Python and your first GitHub contributions.

## Before You Start

1. Install Python 3.8 or newer.
2. Install Git.
3. Create a GitHub account if you do not already have one.
4. Fork this repository on GitHub, then clone your fork:

```bash
git clone https://github.com/YOUR-USERNAME/quiz-game.git
cd quiz-game
```

Replace `YOUR-USERNAME` with your GitHub username.

## Create a Branch

Create a separate branch for each feature or fix. Use a short, descriptive name:

```bash
git checkout -b add-new-questions
```

Examples of branch names:

- `add-new-questions`
- `fix-score-message`
- `improve-readme`

## Set Up and Make Your Change

Create and activate the virtual environment described in [Readme.md](Readme.md), then edit the files needed for your idea.

Keep your change focused. For example, you could:

- Add new quiz questions.
- Improve the score message.
- Fix a spelling mistake.
- Improve the instructions.

## Test Your Change

Start the game and try it from beginning to end:

```bash
python main.py
```

Check that your change works and that existing quiz behavior still works. You can also check Python syntax with:

```bash
python -m compileall main.py questions.py quiz.py utils.py
```

## Commit Your Change

See which files changed:

```bash
git status
```

Add your changes and create a clear commit:

```bash
git add .
git commit -m "Add new quiz questions"
```

Use a message that briefly explains what you changed.

## Push Your Branch

Send your branch to your GitHub fork:

```bash
git push -u origin add-new-questions
```

Replace `add-new-questions` with your branch name.

## Open a Pull Request

1. Open your fork on GitHub.
2. Click **Compare & pull request**.
3. Give the pull request a clear title.
4. Describe what you changed and how you tested it.
5. Submit the pull request.

Someone can then review your work and suggest improvements. Be open to feedback and update your branch if needed.

## Helpful Git Commands

```bash
git status                 # See changed files
git diff                   # Review your changes
git branch                 # List branches
git pull origin main       # Get the latest changes
git switch main            # Switch back to the main branch
git switch -c new-branch  # Create and switch to a new branch
```

Thank you for contributing!
