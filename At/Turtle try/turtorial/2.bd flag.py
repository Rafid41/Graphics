import turtle


def buttonclick(x,y):
    print("{} , {}".format(x,y))


t=turtle.Turtle()

t.penup()
t.goto(-150,100)

t.fillcolor("green")
t.begin_fill()

t.pendown()
for i in range (2):
    t.forward(300)
    t.right(90)
    t.forward(180)
    t.right(90)

t.end_fill()
t.penup()

#circle
t.goto(-15.0 , -49.0)
t.fillcolor("red")

t.pendown()


turtle.onscreenclick(buttonclick, 1)

t.begin_fill()
t.circle(60)
t.end_fill()


turtle.done()


