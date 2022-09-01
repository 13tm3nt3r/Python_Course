# Guess the number from 1 to 10
import random


def guess_number():
    random_n = random.randrange(9) + 1
    user_n = int(input("Guess the number! \nWrite your guess here: "))

    if (user_n < 1) or (user_n > 10):
        print("The range between you have to choose the number is from 1 to 10!")
    if user_n == random_n:
        print("Congrats! You are right!!")
    if user_n != random_n:
        print("Ouch! The number you were supposed to guess was {}".format(random_n))


guess_number()
