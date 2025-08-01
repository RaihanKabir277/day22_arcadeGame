
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)


# tim = Turtle()
# tim.color("white")
# tim.shape("circle")
# tim.forward(100)

ball = Ball()
r_paddle = Paddle((350, 0)) 
l_paddle = Paddle((-350, 0)) 
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #its should bouncing
        ball.bounce_y()
    
    #detect collision with both paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() <-320:
        ball.bounce_x()
        
    #miss the right puddle 
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #miss the left puddle 
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()


