import colorgram
from turtle import Turtle, Screen
from random import choice, randint

#Extract color from image
# colors = colorgram.extract('image2.jpg', 30)
# list_color = []
# def color_tuple(r,g,b):
#     return (r,g,b)
#
# for color in colors:
#     color_red = color.rgb.r
#     color_green = color.rgb.g
#     color_blue = color.rgb.b
#     list_color.append(color_tuple(color_red,color_green,color_blue))
#save the color extracted
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198), (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210), (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162), (156, 212, 190), (87, 46, 33), (37, 45, 83)]

timy = Turtle()
screen = Screen()
screen.colormode(255)

timy.speed('fastest')
dot_size = 20
square_size = 10
y_position = -250
x_position = -250
space_dots = 25

for y in range (square_size):
    timy.penup()
    timy.setpos(x_position, y_position)
    for x in range (square_size):
        timy.pendown()
        timy.dot(dot_size, choice(color_list))
        timy.penup()
        timy.fd(dot_size+space_dots)

    y_position += dot_size+space_dots




screen.exitonclick()
