from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self)-> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()

    def l_point(self):
        self.l_score+=1

    def r_point(self):
        self.r_score+=1
    
    def update_score(self):
        self.speed(10)
        self.clear()
        self.goto(-150,180)
        self.write(self.l_score,align='center',font=('Courier',60,'normal'))
        self.goto(150,180)
        self.write(self.r_score,align='center',font=('Courier',60,'normal'))

