from turtle import Turtle,Screen

timmy = Turtle()
mu_screen = Screen()

# MEthod 1
for dashes in range(20):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

#  Method 2
for dashes in range(20):

    timmy.color("black")
    timmy.forward(5)
    timmy.color("white")
    timmy.forward(5)
    timmy.color("black")

my_screen = Screen()
my_screen.exitonclick()