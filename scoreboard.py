from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.pencolor("white")
        self.hideturtle()
        self.score = 0
        self.penup()

        #self.goto(0, 0)

    def add(self):
        self.score += 1

    def refresh(self):
        self.clear()
        self.write(f"Score {self.score}", False, "center",("Arial", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center",("Arial", 18, "normal"))




