from turtle import Turtle, Screen

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake by CK")
starting_positions = [(0,0), (-20,0), (-40,0)]
for pos in starting_positions:
    new_t = Turtle(shape="square")
    new_t.color("white")
    new_t.goto(pos)


screen.exitonclick()