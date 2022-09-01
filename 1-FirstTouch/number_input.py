# Program to know, from 3 user input numbers, which is the min
def number_input():
    number_1, number_2, number_3 = input("Write three numbers separated by spaces: ").split()

    print("The minimum number between those is: {} and the max is: {}".format(
        min(number_1, number_2, number_3), max(number_1, number_2, number_3))
    )


number_input()
