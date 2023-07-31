import turtle

t=turtle.Turtle()

n=int(input("number of sides : "))
s=int(input("side size : "))


for i in range(n):
    t.forward(s)
    t.left(360/n)

turtle.done()