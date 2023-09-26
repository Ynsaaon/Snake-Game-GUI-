from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/yanisa/Desktop/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/yanisa/Desktop/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0

    def get_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
