# This cheese quiz would have 3 questions with 3 given answers (A=30p, B=15p and C=0p)


def quiz():
    user_score = 0

    # Title
    title = "Welcome to the CHEESE QUIZ!!"
    length = len(title)
    # print("{} \n{} \n".format(title, ("-" * length)))
    print("\n" + title + "\n" + "-"*length)

    # Questions
    q1 = input("\nQuestion 1: \nA - . \nB - . \nC - . \n>>>>> ")
    user_score = score(q1, user_score)
    q2 = input("\nQuestion 2: \nA - . \nB - . \nC - . \n>>>>> ")
    user_score = score(q2, user_score)
    q3 = input("\nQuestion 3: \nA - . \nB - . \nC - . \n>>>>> ")
    user_score = score(q3, user_score)

    print("\nYour final score was: {}".format(user_score))
    if user_score > 30:
        print("You LOVE cheese!")
    elif 15 < user_score <= 30:
        print("You LIKE cheese!")
    else:
        print("You HATE cheese!")


def score(question_number, user_score):
    if question_number == "A":
        user_score += 30
    elif question_number == "B":
        user_score += 15
    elif question_number == "C":
        user_score += 0
    else:
        print("Your option was not correct")
        exit()

    return user_score


quiz()
