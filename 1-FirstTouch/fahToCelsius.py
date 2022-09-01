# Convert Fahrenheit to Celsius

def fah_to_cel():
    # Formula: (fah-32)*5/9=cel
    fah = int(input("Write a Fahrenheit temperature to convert it to Celsius: "))
    print("Your Fahrenheit temperature is equivalent to {:.0f}º Celsius degrees".format((fah-32)*5/9))


fah_to_cel()
