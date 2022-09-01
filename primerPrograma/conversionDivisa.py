# Ask the user which divisas wants to convert

def convert_divisa():
    dolar_euro = 1.00
    pound_euro = 1.18
    euro_pound = 0.85
    dolar_pound = 0.85
    pound_dolar = 1.18

    print("Hello! What divisa do you want to use? \n"
          "- Dolar \n"
          "- Euro \n"
          "- Pound \n")
    initial_divisa = input(">>> ")

    print("And what divisa do you want to covert {} to? \n"
          "- Dolar \n"
          "- Euro \n"
          "- Pound \n".format(initial_divisa))
    final_divisa = input(">>> ")

    quantity_i = float(input("Write the quantity of the initial divisa that you want to convert: "))
    quantity_f = 0
    if (initial_divisa == "Dolar" and final_divisa == "Euro") or (initial_divisa == "Euro" and final_divisa == "Dolar"):
        quantity_f = quantity_i*dolar_euro
    elif initial_divisa == "Pound" and final_divisa == "Euro":
        quantity_f = quantity_i*pound_euro
    elif initial_divisa == "Euro" and final_divisa == "Pound":
        quantity_f = quantity_i*euro_pound
    elif initial_divisa == "Pound" and final_divisa == "Dolar":
        quantity_f = quantity_i*pound_dolar
    elif initial_divisa == "Dolar" and final_divisa == "Pound":
        quantity_f = quantity_i*dolar_pound
    else:
        print("There is an error with the answer you give to me. Revise it, please.")

    print("At the moment, {:.2f} of {} is equivalent to {:.2f} of {}".format(
        quantity_i, initial_divisa, quantity_f, final_divisa))


convert_divisa()
