import turtle as t
import random

timmy = t.Turtle()
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")
directions = [90,0,180,270]
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
#  method 1
for walk in range(200):
    timmy.forward(30)
    timmy.color(random_color())
    timmy.left(random.choice(directions))
    timmy.right(random.choice(directions))

#  Methos 2
for walk in range(200):
    timmy.forward(30)
    timmy.color(random_color())
    timmy.setheading(random.choice(directions))


my_screen = t.Screen()
my_screen.exitonclick()