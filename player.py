from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVE_INCREMENT = 2


class Player:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.pu()
        self.turtle.goto(STARTING_POSITION)
        self.turtle.setheading(90)
        self.player_speed = MOVE_DISTANCE

    def go_up(self):
        self.turtle.fd(self.player_speed)

    def go_down(self):
        if self.turtle.ycor() > -280:
            self.turtle.backward(self.player_speed)

    def increase_player_speed(self):
        self.player_speed += MOVE_INCREMENT

    def reset_position(self):
        self.turtle.goto(STARTING_POSITION)

    def get_y(self):
        return self.turtle.ycor()