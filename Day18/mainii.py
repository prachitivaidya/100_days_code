import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(sides):
    for _ in range(sides):
        angel = 360 / sides
        tim.forward(100)
        tim.right(angel)


for shape_side in range(3, 15):
    tim.color(random.choice(colours))
    draw_shape(shape_side)