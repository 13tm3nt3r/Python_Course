# In this program we are gonna count vowels and consonants

vowels_i = ["a", "e", "i", "o", "u"]
phrase = "Hello, my name is Laura"

consonants = 0
consonants_array = []
vowels_found = 0
vowels_array = []

for i in phrase:
    if i not in vowels_i:
        if i != " " and i != ",":
            consonants += 1
            consonants_array.append(i)
    else:
        vowels_found += 1
        vowels_array.append(i)

print("Phrase: {}\n"
      "Total vowels: {} = {}\n"
      "Total consonants: {} = {}".format(phrase, vowels_array, vowels_found, consonants_array, consonants))
