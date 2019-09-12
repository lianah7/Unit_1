import turtle
turtle.speed(0)
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
turtle.forward(130)
turtle.right(160)
turtle.pendown()
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

for x in range(5):
    turtle.forward(70)
    turtle.left(144)

turtle.penup()
turtle.forward(200)
turtle.pendown()

for x in range(4):
    turtle.forward(90)
    turtle.left(90)
turtle.right(20)

for x in range(4):
    turtle.forward(90)
    turtle.left(90)
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

for x in range(4):
    turtle.forward(80)
    turtle.left(90)
turtle.right(120)

turtle.exitonclick()