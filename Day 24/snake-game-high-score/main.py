from tracemalloc import Snapshot
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
"""
1. Create a Snake Body
"""
snake = Snake()
# Note: We have mode moved the snake code into a separate class

"""
class inheritance concepts- creating food
"""
food = Food()

"""
class to track scoreboard
"""
scoreboard = Scoreboard()

"""
3. how to control the snake with keypress
"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right, "Right")

"""
2. Move the snake and turning the snake
"""
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    """
        4. snake collision detection with food using distance method.
    """
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # 5. Create a scoreboard class to hold the scoreboard
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    # if head collides with any segment in the tail:
        #trigger game over
    # the below concepts can be made easier with slicing concept

    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

