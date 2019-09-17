# by Liana Hill
# September 17, 2019
# This program creates four octagons in four different colors and locations

import turtle


# This function makes an octagon
def draw_octagon(color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(8):
        turtle.fd(60)
        turtle.rt(45)
    turtle.end_fill()


# This function moves turtle to chosen location
def go_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# The following lines create octagons in new locations and colors
draw_octagon("teal")
go_to(200, 0)

draw_octagon("medium purple")
go_to(200, 200)

draw_octagon("medium turquoise")
go_to(0, 200)

draw_octagon("indigo")

# This line shows the program stays on screen until click
turtle.exitonclick()