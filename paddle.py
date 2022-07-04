from turtle import Turtle

STARTING_POSITIONS = [(350, 0), (-350, 0)]
MOVE_DISTANCE = 20



class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=10, stretch_wid=1)
        self.penup()
        self.goto(position)
        self.speed("fastest")

    def left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())