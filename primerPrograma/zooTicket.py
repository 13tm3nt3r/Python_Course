# To enter to the zoo with a 25% discount, one of the next options has to be satisfied:
# - Be between 25-35 yo
# - Have <10 yo
# - Have >65 yo
# - Have a numerous family book
# Variables: years (int) and carnet ("S"(tudent), "P"(ensionist), "F"(amily), "N"(othing))

def discount():
    ticket = 10
    have_discount = True

    enter = input("Hey!! Do you want to enter to the zoo? [Yes/No] ")
    if enter != "Yes":
        print("Ok!! So see you later!!")
        exit(1)
    years = int(input("How old are you? "))
    disc = input("And do you have any discount? \n- \"S\"tudent \n- \"P\"ensionist \n- \"F\"amily numerous \n- "
                 "\"N\"othing \n: ")
    if (25 >= years <= 35 and disc == "S") or \
            (years < 10 and disc == "N") or \
            (years > 65 and disc == "P") or \
            (disc == "F"):
        print("You have a 25% of discount!")
    else:
        print("Sorry, so would have to pay the complete ticket price")
        have_discount = False

    if have_discount:
        print("The price of the ticket is of {}€".format(ticket-(ticket*0.25)))
    else:
        print("The price of the ticket is of {}€".format(ticket))


discount()
