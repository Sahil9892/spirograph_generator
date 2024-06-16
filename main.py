import turtle as t
import random

timmy = t.Turtle()
timmy.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(gap):
    for i in range(int(360/gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)

gap = int(input("How much degree gap do you want between cicles: "))

draw_spirograph(gap)








t.exitonclick()