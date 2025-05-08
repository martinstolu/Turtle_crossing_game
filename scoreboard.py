from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_FONT = ("Courier", 12, "normal")


class Scoreboard:
    def __init__(self):
        self.sc = Turtle()
        self.sc.pu()
        self.sc.hideturtle()
        self.sc.goto(x= -280, y= 280)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.sc.clear()
        self.sc.write(arg=f"level: {self.level}", align="left",
                   font=LEVEL_FONT)

    def increase_scoreboard(self):
        self.level+=1
        self.update_scoreboard()


    def game_over(self):
        self.sc.goto(0, 0)
        self.sc.write(arg="Game Over", align="center", font=FONT)