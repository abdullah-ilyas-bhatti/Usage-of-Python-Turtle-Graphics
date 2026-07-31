from turtle import Turtle, Screen

timmy = Turtle()
my_screen = Screen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def move_up():
    timmy.left(10)
    

def move_down():
    timmy.right(10)
    


my_screen.listen()
my_screen.onkey(fun=move_forward,key= "w")
my_screen.onkey(move_backward, "s")
my_screen.onkey(move_up, "d")
my_screen.onkey(move_down, "a")

my_screen.exitonclick()