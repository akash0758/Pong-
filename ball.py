from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.x_move = 10
        self.y_move = 20

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        position = (x, y)
        self.goto(position)
    
    def paddle_collision(self):
        self.x_move *= -1
    
    