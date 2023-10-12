from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        head = Turtle("square")
        head.color("white")
        head.penup()
        head.goto(position)
        self.segments.append(head)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        for seg_number in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_number - 1].xcor()
            y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(x, y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

