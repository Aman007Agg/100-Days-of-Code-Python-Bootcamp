

"""
Unlimited Arguments- *args - tuple
print(type(kwargs))
"""
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,3,5))

"""
**kwargs (keyword arguments)
print(type(kwargs)) - <class 'dict'>
"""
def calculate(n, **kwargs):
    # print(type(kwargs))
    # print(kwargs)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)



