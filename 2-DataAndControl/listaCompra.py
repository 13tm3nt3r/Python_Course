# In this program, a menu would be shown each time and if Q is inserted, the program will stop.

print("\nWellcome to your supermarket automated list!!\n")

lista = []
item = None

while True:
    item = input("What do you want to note to buy in the Supermarket? (Enter 'Q' to end the list) \n"
                  ">>>> ")
    if item == "Q":
        break
    elif item in lista:
        print("{} is already in the list!".format(item))
    else:
        lista.append(item)

print("\nYour supermarket list is:")
for i in lista:
    print(" - {}".format(i))
