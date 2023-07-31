import turtle

t=turtle.Turtle()

t.forward(100)  # 30 unit
t.left(90)  #90 degree

t.forward(100)
t.left(90)


t.forward(100)
t.left(90)


t.forward(100)
t.left(90)
t.penup()





#using loop
t.goto(50,80)
t.pendown()

for i in range(4):
    t.forward(150)
    t.left(90)

turtle.done()