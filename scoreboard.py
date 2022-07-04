from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-180, 350)
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.lives = 3
        self.update_score_display()


    def update_score_display(self):
        self.write(f"Score: {self.score}   Lives: {self.lives}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_score_display()


    def update_lives(self):
        self.clear()
        self.lives -= 1
        self.update_score_display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def you_win(self):
        self.goto(0, 0)
        self.write("YOU WIN", align="center", font=FONT)
