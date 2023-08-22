from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('orange')
        self.score = 0
        self.goto(position)
        self.write(f'score: {self.score}', font=('Calibri Body', 18, 'normal'))
    
    def update(self):
        self.score += 1
        self.clear()
        self.write(f'score: {self.score}', font=('Calibri Body', 18, 'normal'))
        
        
