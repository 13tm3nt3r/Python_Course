# Print the minimum and maximum number in a list given by the user

# user_list = []

numbers = input("Introduce numbers separated by spaces\n>>>>> ")

user_list = [int(numero) for numero in numbers.split(" ")]

# number = int(input("Introduce a number: "))
# user_list.append(number)
#
# while input("Do you wannt to introduce more numbers? [Y/N] ") == "Y":
#     number = int(input("Introduce a number: "))
#     user_list.append(number)

# Select the minimum
minimum = user_list[0]
for i in user_list[1:]:  # From the position 1 in the array/list
    if i < minimum:
        minimum = i

# Select the maximum
maximum = user_list[0]
for i in user_list[1:]:  # From the position 1 in the array/list
    if i > maximum:
        maximum = i

print("\nYour list is: {} \nThe minimum number is: {} and the maximum is {}.".format(user_list, minimum, maximum))
