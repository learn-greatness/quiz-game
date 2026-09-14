def show_score(score, total):
    print()
    print("--------------------")
    print("Quiz Finished!")
    print("Your score:", score, "/", total)

    percentage = (score / total) * 100

    print("Percentage:", percentage, "%")

    if percentage == 100:
        print("Perfect score!")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Keep practicing!")

    print("--------------------")