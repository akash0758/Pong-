from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

import time

import turtle


turtle.tracer(0)
screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=500)

l_paddle = Paddle((-280,0))
p1_score = ScoreBoard((-150,210))
p2_score = ScoreBoard((150,210))
r_paddle = Paddle((275,0))

poo = Ball()

while True:
    turtle.update()
    time.sleep(0.1)
    poo.move()
    if poo.ycor()>240 or poo.ycor()<-240:
        poo.y_move *= -1

    if poo.xcor()>295:
        poo.goto((0,0))
        poo.x_move *= -1
        p1_score.update()

    if poo.xcor()< -300:
        poo.goto((0,0))
        poo.x_move *= -1
        p2_score.update()
    
    if poo.distance(l_paddle) < 35 or poo.distance(r_paddle) <35:
        poo.paddle_collision()



        

    screen.listen()

    screen.onkeypress(key='Up', fun=r_paddle.up)
    screen.onkeypress(key='Down', fun=r_paddle.down)
    screen.onkeypress(key='w', fun=l_paddle.up)
    screen.onkeypress(key='s', fun=l_paddle.down)








screen.exitonclick()