from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def update_scoreboard(self):
        self.clear()
#        self.reset()
        self.write(f"Score: {self.score} High Score: {self.high_score}", self.color("white"), align="center", font=("Arial", 24, "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
#                self.high_score = int(data.write)
                data.write(f"{self.high_score}")
#        self.clear()
        self.score = 0
        self.update_scoreboard()