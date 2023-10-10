import turtle
import random
turtle.colormode(255)
t = turtle.Turtle()
t.penup()
t.speed("fastest")
t.hideturtle()
color_list = [(43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253), (160, 3, 82), (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251), (211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56), (216, 114, 171), (16, 127, 144), (85, 248, 252), (188, 39, 109), (23, 5, 107), (8, 209, 215), (99, 8, 50), (231, 163, 205), (204, 119, 35), (112, 6, 4)] # you can import this list of colors from another image using cologram.

t.setheading(225)
t.forward(300)
t.setheading(0)
num_of_dots = 100


for dot_count in range(1, num_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
