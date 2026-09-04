from questions import questions
from quiz import run_quiz
from utils import show_score


def main():
    print("====================")
    print("     PYTHON QUIZ")
    print("====================")

    name = input("Enter your name: ")

    print()
    print("Hello,", name)
    print("Let's start the quiz!")

    score = run_quiz(questions)

    show_score(score, len(questions))


if __name__ == "__main__":
    print("Starting Game...")
    # main()