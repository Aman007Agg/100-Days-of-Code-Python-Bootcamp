def is_prime(num):
    # Prime numbers must be grater than 1
    if num <= 1:
        return False
    # Check divisibility from 2 up to sqrt(num)
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
print(is_prime(73))