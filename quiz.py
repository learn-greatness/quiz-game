def ask_question(question_data):
    print()
    print(question_data["question"])

    options = question_data["options"]

    for i in range(len(options)):
        print(i + 1, ".", options[i])

    while True:
        choice = input("Enter your answer (1-4): ")

        if choice in ["1", "2", "3", "4"]:
            break

        print("Please enter a number between 1 and 4.")

    selected_answer = options[int(choice) - 1]

    if selected_answer == question_data["answer"]:
        print("Correct!")
        return True

    print("Wrong!")
    print("Correct answer:", question_data["answer"])

    return False


def run_quiz(questions):
    score = 0

    for question in questions:
        correct = ask_question(question)

        if correct:
            score += 1

    return score