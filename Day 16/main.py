from turtle import Turtle, Screen
from another_module import table

print(table)

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("Red")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight) # attributes
my_screen.exitonclick()   # calling a method

