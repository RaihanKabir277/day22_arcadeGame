
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # self.tim = Turtle("square")
        # self.tim.color("white")
        # self.tim.penup()
        # self.tim.shapesize(5, 1)
        # self.tim.goto(350, 0)
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.position = position
        self.goto(self.position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

