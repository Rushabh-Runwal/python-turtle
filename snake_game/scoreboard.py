from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = self.get_high_score()
        self.score = 0
        self.hideturtle()
        self.goto(0, 280)
        self.color('#fff')
        self.update()

    def get_high_score(self):
        with open('high_score.txt',mode = 'r') as f:
            return int(f.read())

    def update(self):
        self.clear()
        self.write(f'Score = {self.score}  High Score={self.get_high_score()}', move=False, align="center", font=("Arial", 14, "normal"))

    def refresh(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode = 'w') as f:
                f.write(str(self.score))

        self.score = 0
        self.update()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('Game Over.', move=False, align="center", font=("Arial", 14, "normal"))

    def increment(self):
        # self.clear()
        self.score += 1
        self.update()
