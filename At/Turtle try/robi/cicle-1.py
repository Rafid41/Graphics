import random
from turtle import Turtle, Screen, colormode

t = Turtle()
t.shape("turtle")
t.speed("fastest")
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_circle(angle):
    for shape in range(int(360 / angle)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + angle)


draw_circle(2)
s = Screen()
s.exitonclick()