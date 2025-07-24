from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("welcome to the pong game👾👾 ")
screen.tracer(0)

right_paddle=Paddle((350,0))
left_paddle=Paddle((-350,0))
ball=Ball()
score_board=Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

game_is_on=True
while  game_is_on:
    time.sleep(ball.speed_up)
    screen.update()
    ball.ball_move()
#  detection for collision of ball with wall
    if ball.ycor()>270 or ball.ycor()<-270:
        ball.bounce_y()
    #        we need to bounce when we collide with the paddle
    if ball.distance(right_paddle)<50 and ball.xcor()>340 or ball.distance(left_paddle)<50 and ball.xcor()<-340:
        print("touches both sides")
        ball.bounce_x()
#  resetting when doesn't collide with right-paddle(misses)
    if ball.xcor()>380:
        ball.reset_position()
        score_board.left_point()
#     resetting when ball misses left_paddle
    if ball.xcor()<-380:
        ball.reset_position()
        score_board.right_point()


screen.exitonclick()
