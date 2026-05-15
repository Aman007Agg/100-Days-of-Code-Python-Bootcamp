import turtle as t
import random
from turtle import Turtle

from higher_order_function import add,sub, multiply, divide, calculator

"""
calculate is the higher order function
"""
add_result = calculator(2, 3, add)
sub_result = calculator(2, 3, sub)
divide_result = calculator(2, 3, divide)
multiply_result = calculator(2, 3, multiply)

print(add_result, sub_result, divide_result, multiply_result)

# timmy = t.Turtle(shape="turtle")
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)


screen = t.Screen()

"""
Event and Listeners
"""
# def move_forward():
#     timmy.forward(10)
#
# screen.listen()
# screen.onkey(key ="space", fun=move_forward)
#
# screen.exitonclick()

"""
Etch a Sketch
"""
# def move_forward():
#     timmy.forward(10)
#
# def move_backward():
#     timmy.backward(10)
#
# def move_turn_left():
#     # new_heading = timmy.heading() + 10
#     # timmy.setheading(new_heading)
#     timmy.left(10)
#
# def move_turn_right():
#     timmy.right(10)
#
# def clear():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
#
# screen.listen()
# screen.onkey(key ="w", fun=move_forward)
# screen.onkey(key ="s", fun=move_backward)
# screen.onkey(key ="a", fun=move_turn_left)
# screen.onkey(key ="d", fun=move_turn_right)
#
# screen.exitonclick()


"""
Turtle Race Project
"""
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
# print(user_bet)
colors = ["red", "orange", "yellow", "green" , "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True




while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won!, The {winning_color} turtle is the winner!")
            else:
                print(f"You lose!, The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()