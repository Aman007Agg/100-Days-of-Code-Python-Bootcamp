print(len("12345"))

# Primitive Data Types
print(type("Aman"))
print(type(123))
print(type(3.14))
print(type(True))

# Data Type Conversion - implicit Conversion
print("Before Conversion: " + "123" + "123")
print("After Conversion:")
print(int("123") + int("123"))


user_name = input("Enter your name")
length_of_name = len(user_name)

print(type("Number of letters in your name: ")) #str
print(type(length_of_name)) #int

print("Number of letters in your name: " + str(length_of_name))