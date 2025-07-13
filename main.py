
from turtle import Screen
from paddle import Paddle
from ball import Ball
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


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()


