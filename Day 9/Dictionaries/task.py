programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

for key in programming_dictionary:
    print(key) # key
    print(programming_dictionary[key]) # value

for values in programming_dictionary.values():
    print(values)


print("\n" + programming_dictionary["Bug"])

empty_dictionary = {}
empty_dictionary["Loop"] = "This is a Loop"
print(empty_dictionary)

# Wipe an existing dictionary
empty_dictionary = {}
print(empty_dictionary)