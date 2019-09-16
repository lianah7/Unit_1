import turtle


# octagon function
def draw_octagon():
    for x in range(8):
        turtle.fd(50)
        turtle.rt(45)


# goto function
def go_to(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


# creates a bright blue octagon
turtle.color("dodger blue")
turtle.begin_fill()
draw_octagon()
turtle.end_fill()
go_to(200,5)

# makes a bright purple octagon
turtle.color("medium slate blue")
turtle.begin_fill()
draw_octagon()
turtle.end_fill

# program stays on screen until click
turtle.exitonclick()