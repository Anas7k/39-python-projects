from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=800, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color: ")
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
y_position = [-190, -110, -30, 40, 110, 190]
all_turtles = []
for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.shapesize(stretch_wid=2, stretch_len=2)
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-380, y=y_position[i])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 350:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
