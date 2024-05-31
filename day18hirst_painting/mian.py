###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

# rgb_colors = []
# colors = colorgram.extract('img.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_c = (r, g, b)
#     rgb_colors.append(new_c)


import  turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(201, 158, 113), (66, 105, 122), (135, 160, 171), (135, 173, 163), (151, 85, 53), (123, 83, 96)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dots  in range(1, num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dots % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = t.Screen()
screen.exitonclick()