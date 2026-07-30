from turtle import Turtle,Screen
import random

timmy = Turtle()
timmy.shape("turtle")

#  Method 1
for triangle in range (0,3):
    timmy.color("red")
    timmy.forward(100)
    timmy.left(120)

for square in range(0,4):
    timmy.forward(100)
    timmy.color("green")
    timmy.left(90)

for pentagon in range(0,5):
    timmy.forward(100)
    timmy.color("purple")
    timmy.left(72)

for hexagon in range(0,6):
    timmy.forward(100)
    timmy.color("orange")
    timmy.left(60)

for heptagon in range(0,7):
    timmy.forward(100)
    timmy.color("blue")
    timmy.left(51)

for octagon in range(0,8):
    timmy.forward(100)
    timmy.color("brown")
    timmy.left(45)

for nonagon in range(0,9):
    timmy.forward(100)
    timmy.color("grey")
    timmy.left(40)

for decagon in range(0,10):
    timmy.forward(100)
    timmy.color("coral2")
    timmy.left(36)


#  Method 2
def draw_shape(sides):
    degree = 360 / sides
    for shapes in range(sides):
        timmy.forward(100)
        timmy.left(degree)

colors = [ "red", "orange", "yellow", "green", "blue", "indigo", "purple"]
for shape_sides in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(shape_sides)

my_screen = Screen()
my_screen.exitonclick()
