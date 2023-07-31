import turtle

t=turtle.Turtle()


t.speed(300)



t.left(-45)     # or t.seth(-45)

for i in range(90):
    t.backward(2)
    t.left(1)

for i in range(90):
    t.backward(1)
    t.left(1)


for i in range(90):
    t.backward(2)
    t.left(1)

for i in range(90):
    t.backward(1)
    t.left(1)

turtle.done()