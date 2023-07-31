import turtle

t=turtle.Turtle()

t.penup()
t.goto(-200,-200)
t.pendown()


def showAxis(x,y):
    print("{} , {}".format(x,y))


turtle.onscreenclick(showAxis, 1)


for i in range(4):
    t.forward(300)
    t.left(90)
    print(t.pos())

t.goto(-80.0 , -91.0)

for i in range(4):
    t.forward(300)
    t.left(90)


print(t.pos())
t.seth(90)
t.forward(300)


turtle.done()