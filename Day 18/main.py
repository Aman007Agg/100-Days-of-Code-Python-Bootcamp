import random
from turtle import Turtle, Screen
import turtle as t

# from turtle import *

timmy = t.Turtle()
t.colormode(255)
# colours = ["medium aquamarine", "red", "blue", "green", "yellow", "DeepSkyBlue", "wheat", "SlateGray"]
# directions = [0, 90, 180, 270]
# timmy.pensize(10)
timmy.speed("fastest")


# timmy.shape("turtle")
# timmy.color("red")

"""
Created a dash line
"""
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#
# screen = Screen()
# screen.exitonclick()


"""
Created a Square
"""
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
#
# screen = Screen()
# screen.exitonclick()

"""
Draw shapes using turtle
"""
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side in range(3, 11):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side)

"""
Draw a Random Walk
"""
# for _ in range(200):
#     timmy.color(random.choice(colours))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#
#
# screen = Screen()
# screen.exitonclick()



"""
Draw a Random Walk with random colours
"""
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_colour = (r, g, b)
#     return random_colour
#
# for _ in range(200):
#     # timmy.color(random.choice(colours))
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#
# screen = Screen()
# screen.exitonclick()


"""
Draw a Spiral graph
"""
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


def draw_spiralgraph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + 10)

draw_spiralgraph(5)

screen = Screen()
screen.exitonclick()
