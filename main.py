import colorgram
from turtle import Turtle, Screen

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

for x in range (100):
    timy.setpos(x+10,0)




screen.exitonclick()

