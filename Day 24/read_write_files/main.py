# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# it will automatically close the file.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="w") as file:
    file.write("New Text check.")

with open("my_file.txt", mode="a") as file:
    file.write("\n Hi Aman.")