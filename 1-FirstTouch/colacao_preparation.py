# For this code, the steps needed to prepare a cacao are described
def prepare_cacao():
    print("Im going to the kitchen")

    have_milk = input("Do I have milk in the fridge? Yes or No: ")
    milk = boolean_input(have_milk)
    have_cacao = input("Do I have cacao? Yes or No: ")
    cacao = boolean_input(have_cacao)

    if milk and cacao:
        print("Pour the milk in a glass")
        print("Pour the cacao in the milk")
        print("CONGRATULATIONS! Now you can drink your milk with cacao :)")
    else:
        print("I have to go to the supermarket", end="", flush=True)
        if not milk:
            print(" and I have to buy milk", end="", flush=True)
        if not cacao:
            print(" and I have to buy cacao", end="", flush=True)


def boolean_input(boolean):
    if boolean == "Yes":
        return True
    if boolean == "No":
        return False


prepare_cacao()
