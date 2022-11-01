import time
from turtle import Turtle,Screen
from two_paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle=Turtle()
ball=Ball()
score=Scoreboard()

r_paddle=Paddle((270,0))
l_paddle=Paddle((-270,0))
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on=True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #ball bounce
    if ball.ycor()>280 or ball.ycor() <-280:
        ball.bounce_y()

    #paddle bounce
    if ball.distance(r_paddle) < 50 and ball.xcor()>250:
        ball.bounce_x()
        ball.move_speed-=0.01
    if ball.distance(l_paddle) < 50 and ball.xcor()>-250:
        ball.bounce_x()
        ball.move_speed-=0.01

    #reset the ball for r_paddle
    if ball.xcor()>280:
        ball.reset_position()
        ball.move_speed=0.1
        ball.move()
        score.l_scores()

    #reset the ball for l_paddle
    if ball.xcor()<-280:
        ball.reset_position()
        ball.move()
        score.r_scores()
    score.end_game()
    if score.r_score==5 or score.l_score==5:
        game_on=False
screen.exitonclick()
