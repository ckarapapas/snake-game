from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake by CK")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.refresh()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        print("Yummyy....")
        food.refresh()
        snake.extend()
        scoreboard.add()
        scoreboard.refresh()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    new_seg = []
    for seg in snake.segments[1:]:
        new_seg.append(seg)
    poss = []
    for seg in new_seg:
        poss.append(seg.position())
    if snake.head.position() in poss:
        game_is_on = False
        scoreboard.game_over()





screen.exitonclick()