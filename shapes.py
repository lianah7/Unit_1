import turtle

turtle.speed(8)

# function for making a square
def draw_square():
    for x in range(4):
        turtle.fd(100)
        turtle.right(90)


# function for making a triangle
def draw_triangle():
    for x in range(3):
        turtle.forward(100)
        turtle.left(120)


turtle.penup()
turtle.left(90)
turtle.forward(200)
turtle.pendown()

for x in range(4):
    turtle.left(90)
    turtle.forward(90)

turtle.penup()
turtle.forward(140)
turtle.right(160)
turtle.pendown()

# makes a pentagon
turtle.forward(90)
turtle.left(72)
turtle.forward(90)
turtle.left(72)
turtle.forward(90)
turtle.left(72)
turtle.forward(90)
turtle.left(72)
turtle.forward(90)

turtle.penup()
turtle.forward(300)
turtle.pendown()

turtle.circle(60)
turtle.left(90)

turtle.penup()
turtle.forward(300)
turtle.left(50)
turtle.pendown()

# makes a square
for x in range(5):
    turtle.forward(70)
    turtle.left(144)

turtle.penup()
turtle.forward(200)
turtle.pendown()

# following lines make many squares
draw_square()
turtle.right(20)

draw_square()
turtle.right(20)

for x in range(4):
    turtle.forward(90)
    turtle.left(90)

turtle.right(20)
for x in range(4):
    turtle.forward(90)
    turtle.left(90)

turtle.right(50)
turtle.penup()
turtle.forward(160)
turtle.pendown()
turtle.seth(180)

#makes a house
turtle.color("turquoise")
turtle.begin_fill()

for x in range(4):
    turtle.forward(80)
    turtle.left(90)

turtle.end_fill()
turtle.color("blue violet")
turtle.begin_fill()
turtle.right(60)
turtle.forward(80)
turtle.left(120)
turtle.forward(80)
turtle.seth(180)
turtle.end_fill()
turtle.penup()
turtle.forward(140)
turtle.pendown()
turtle.seth(180)
turtle.end_fill()

turtle.exitonclick()