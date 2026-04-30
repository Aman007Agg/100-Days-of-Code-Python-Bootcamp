# This will print out each of the numbers 1 - 9. So the range can also be expressed like this:
# a <= range(a, b) < b
for number in range(1, 10):
    print(number)


# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
total_number = 0
for number in range(1, 101):
     total_number += number

print(total_number)