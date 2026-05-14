import random
from doctest import script_from_examples

import colorgram
import turtle as turtle_module

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# # print(colors)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
color_list = [(207, 163, 103), (241, 246, 242), (154, 76, 43), (237, 239, 244), (223, 200, 136), (50, 92, 126), (175, 148, 38), (130, 161, 186), (141, 38, 19), (200, 95, 71), (50, 121, 94), (11, 94, 68), (146, 175, 147), (71, 49, 39), (160, 145, 159), (83, 74, 75), (55, 48, 52), (20, 81, 90), (30, 65, 78), (231, 177, 162), (183, 203, 172), (41, 66, 91), (14, 73, 59), (99, 142, 131), (66, 62, 64), (177, 191, 210), (107, 128, 154), (69, 63, 56)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()

