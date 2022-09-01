# Check if the input has uppercase letters

user_phrase = input("Write your favorite phrase \n>>>> ")

uppercase = 0

for letter in user_phrase:
    if letter.isupper():
        uppercase += 1

print("The number of uppercases in your phrase is {}".format(uppercase))
