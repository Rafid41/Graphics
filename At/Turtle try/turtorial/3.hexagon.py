import turtle

ws=turtle.Screen()
t=turtle.Turtle()

t.fillcolor("#000000")

t.begin_fill()

for i in range(6):
    t.forward(100)
    t.left(300)

t.end_fill()

turtle.done()