# Show the multiplication table of a given number

user_n = int(input("Write the number which you want its multiplication table: "))

print("The following operations have a pair number as a result:")
for i in range(0, 11):
    result = user_n*i
    if (result % 2) == 0:
        print("{} x {} = {}".format(user_n, i, result))