# import colorgram
#
# color_rgb = []
# colors = colorgram.extract("2012_0112_Hirst_large.jpg", 30)
#
# for color in colors:
#     # r = color.rgb.r
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     color_rgb.append(new_color)
#
# print(color_rgb)
from turtle import Turtle, Screen

turtle = Turtle()
turtle.hideturtle()
Screen().screensize(500, 500)
Screen().colormode(255)
turtle.penup()
turtle.goto(-200, -200)
# Screen().setworldcoordinates(0, 0, 20, 20)
color_extracted = [(243, 235, 74), (211, 158, 93), (186, 12, 69), (112, 179, 208), (25, 116, 168), (173, 171, 31), (219, 129, 166), (161, 79, 35), (129, 185, 146), (9, 32, 76), (222, 62, 105), (235, 73, 42), (180, 45, 94), (30, 136, 81), (236, 164, 193), (78, 12, 63), (12, 54, 33), (234, 227, 7), (26, 165, 209), (16, 43, 132), (58, 166, 96), (134, 214, 229), (10, 101, 63), (133, 34, 20), (91, 27, 11), (159, 211, 188)]
print(len(color_extracted))
k = 0
turtle.speed(0)
for i in range(10):
    for j in range(10):
        turtle.penup()
        turtle.dot(20, color_extracted[k])
        k += 1
        if k == 26:
            k = 0
        turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(180)


Screen().exitonclick()

