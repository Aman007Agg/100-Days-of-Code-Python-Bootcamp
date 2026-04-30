import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
rand_friends = random.randint(0,4)

if rand_friends == 0:
    print(friends[0])
elif rand_friends == 1:
    print(friends[1])
elif rand_friends == 2:
    print(friends[2])
elif rand_friends == 3:
    print(friends[3])
elif rand_friends == 4:
    print(friends[4])
else:
    print("Incorrect input given")


# Other way to do it. - use random choice function
print(random.choice(friends))

#other simpler way would be
print(friends[rand_friends])