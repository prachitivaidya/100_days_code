import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? enter a color: ")
colours = ["red", "orange", "yellow", "green", "blue", "violet"]
y_positions = [-120, -70, -20, 30, 80, 130]
all_turtles = []
is_race_on = False


# def create_turtle(colour, name, x, y):
#     name = Turtle(shape="turtle")
#     name.color(colour)
#     name.penup()
#     name.goto(x, y)
#
# create_turtle(colours[0],  "tim", -230, -120)
# create_turtle(colours[1], "tom", -230, -70)
# create_turtle(colours[2], "pom", -230, -20)
# create_turtle(colours[3],  "som", -230, 30)
# create_turtle(colours[4], "mon", -230, 80)
# create_turtle(colours[5], "ron", -230, 130)


for ti in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[ti])
    new_turtle.color(colours[ti])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color}")
            else:
                print(f"You've lost! {user_bet}, {winning_color} is the winner")
                is_race_on = False
        rd_dist = random.randint(1, 10)
        turtle.forward(rd_dist)

screen.exitonclick()

