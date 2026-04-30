#Random Module
import random
import my_module

rand_num = random.randint(1, 10)
print(rand_num)

#creating and using module
print(my_module.my_fav_number)

#Random Floating point numbers.
rand_float_num = random.random() #It is always return between 0.0 <= random.random() < 1.0
print(rand_float_num)

#e.g. random.random() * 5 Will generate a random number between 0 and 5.
rand_float_num = random.random() * 9
print(rand_float_num)

#Another way to generate random floating point numbers is to use the uniform() function.
rand_float_num = random.uniform(1,10)
print(rand_float_num)


#Create a coin flip program using what you have learnt about randomisation in Python. It should randomly print "Heads" or "Tails" everytime it is run

rand_int_heads_tails = random.randint(0,1)
print(rand_int_heads_tails)

if rand_int_heads_tails == 0:
    print("Heads")
else:
    print("Tails")
