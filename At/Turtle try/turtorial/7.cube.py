import turtle

t=turtle.Turtle()

l1=[]
l2=[]

t.penup()
t.goto(-200,-200)
t.pendown()

#first sq

for i in range(4):
    t.forward(300)
    t.left(90)

    l1.append(t.pos())

t.seth(45)
t.forward(150)
t.seth(0)  #reset seth


#2nd sq
for i in range(4):
    t.forward(300)
    t.left(90)

    l2.append(t.pos())


for i in range(4):
    t.penup()
    t.goto(l1[i])
    t.pendown()
    t.goto(l2[i])


turtle.done()