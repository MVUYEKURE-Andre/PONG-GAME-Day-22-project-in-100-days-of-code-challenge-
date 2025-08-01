
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.speed_up=0.1

    def ball_move(self):
        ball_x =self.xcor() +self.x_move
        ball_y = self.ycor() + self.y_move
        self.goto(ball_x, ball_y)

    def bounce_y(self):
        self.y_move *=-1

    def bounce_x(self):
        self.x_move *=-1
        self.speed_up*=0.5

    def reset_position(self):
        self.goto(0,0)
        self.speed_up=0.1
        self.bounce_x()
        self.bounce_y()
