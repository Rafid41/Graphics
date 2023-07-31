import turtle

t=turtle.Turtle()

lenth=200

def right_cube():
    t.left(45)
    t.forward(lenth)

    t.right(90 + 45)
    t.forward(lenth)

    t.right(45)
    t.forward(lenth)

    t.right(90 + 45)
    t.forward(lenth)

def left_cube():

    t.left(45)
    t.forward(lenth)

    t.left(90 + 45)
    t.forward(lenth)

    t.left(45)
    t.forward(lenth)

    t.left(90 + 45)
    t.forward(lenth)

def top_cube():
    t.left(45)
    t.forward(lenth)

    t.right(90)
    t.forward(lenth)

    t.right(90)
    t.forward(lenth)




t.fillcolor("blue")
t.color("blue")
t.begin_fill()
right_cube()
t.end_fill()

t.fillcolor("red")
t.color("red")
t.begin_fill()
left_cube()
t.end_fill()

t.fillcolor("yellow")
t.color("yellow")
t.begin_fill()
top_cube()
t.end_fill()



turtle.done()