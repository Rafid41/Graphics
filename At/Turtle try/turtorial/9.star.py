import turtle

s=turtle.Screen()

t=turtle.Turtle()

t.width(5)         # pen marker width
t.right(10)        #full dwawing k 10 degree right  e rotate kore

t.penup()
t.goto(-150,40)
t.pendown()


t.fillcolor("#56ffb8")
t.color("#56ffb8")

x=300

t.begin_fill()
for i in range(5):
    t.forward(x)
    t.right(144)

t.end_fill()

turtle.done()