import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_col():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


tim.speed("fastest")


def draw_spirograph(size):
    for _ in range(int(360/size)):
        tim.color(random_col())
        tim.circle(100)
        tim.setheading(tim.heading()+10)

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()