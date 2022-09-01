def lib_to_euro():
    lib = int(input("Write the number of pounds you want to convert to euros: "))
    conv = float(input("What is the actual conversion? "))

    print("At the moment, {} pounds, with the conversion of {} would be {:.2f}€".format(lib, conv, lib*conv))


lib_to_euro()
