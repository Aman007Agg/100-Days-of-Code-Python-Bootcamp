from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

# my_favourite_calculation = add #You can store a reference to a function as a value to a variable. e.g.
# print(my_favourite_calculation(3, 5))
# print(type(my_favourite_calculation(3, 5)))

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# print(operations[*](4,8))  #it will give 32

def calculator():
    print(logo)
    should_proceed = True
    n1 = int(input("Enter the first number:"))

    while should_proceed:
        # prev_result = 0
        for symbol in operations:
            print(symbol)
        choice = input('Enter the type of mathematical operation - a choice of "+", "-", "*" or "/" ')
        n2 = int(input("Enter the Second number:"))
        # ops = operations[choice]
        # prev_result += ops(n1, n2)
        # print(prev_result)
        answer = operations[choice](n1, n2)
        print(f"{n1} {choice} {n2} = {answer}")
        wants_to_continue = input(f"wants to continue calculating with {answer} : type 'yes' or if not then type 'no' :").lower()
        if wants_to_continue == "yes":
            n1 = answer
        elif wants_to_continue == "no":
            should_proceed = False
            calculator()
        else:
            print("Invalid input, Kindly enter the valid response")
            wants_to_continue = input("wants to continue : type 'yes' or if not then type 'no' :").lower()



calculator()


