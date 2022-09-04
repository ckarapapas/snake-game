from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        for pos in starting_positions:
            self.add_segment(pos)

        self.head = self.segments[0]

    def add_segment(self, pos):
        new_t = Turtle(shape="square")
        new_t.color("white")
        new_t.penup()
        new_t.goto(pos)
        self.segments.append(new_t)
    def move(self):
        for segnum in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segnum-1].pos()[0]
            new_y = self.segments[segnum-1].pos()[1]
            self.segments[segnum].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)
        else:
            pass

    def left(self):
        if self.head.heading() != 0:
            self.segments[0].setheading(180)
        else:
            pass

    def right(self):
        if self.head.heading() != 180:
            self.segments[0].setheading(0)
        else:
            pass

    def down(self):
        if self.head.heading() != 90:
            self.segments[0].setheading(270)
        else:
            pass

    def extend(self):
        self.add_segment(self.segments[-1].position())


