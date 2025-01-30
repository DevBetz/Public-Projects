from turtle import Screen, Turtle

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # self.move()

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9


    def rest_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
