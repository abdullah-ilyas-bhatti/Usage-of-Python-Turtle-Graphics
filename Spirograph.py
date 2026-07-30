import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed('fastest')
directions = [90,180,270]
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb_color = (r, g, b)
    return rgb_color

def spirograph(size):
    for _ in range( int(360 / size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading( timmy.heading() + size )

spirograph(5)    

my_screen = t.Screen()
my_screen.exitonclick()