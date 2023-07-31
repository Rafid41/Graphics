import turtle

t=turtle.Turtle()


t.penup()
t.goto(-200,-200)
t.pendown()



l=200

sz = int(input("polygon edges number : "))
n=int(input("iteration number : "))

angle=360/sz

x=l/n

for i in range(n):
    t.forward(l)
    t.left(angle)

    l-=x

turtle.done()