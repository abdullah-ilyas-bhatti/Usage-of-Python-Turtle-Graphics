from turtle import Turtle, Screen
import random

my_screen = Screen()

my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make a Bet on turtle", prompt="which one turtle you want a bet? Enter a color ")

colors=["red","green","blue","orange","brown","purple"]
points = [-100, -50, -1, 50, 100, 150 ]
all_turtles = []

race_on = False

for num_of_turtle in range (0,6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[num_of_turtle])
    timmy.goto(x=-230,y=points[num_of_turtle])
    all_turtles.append(timmy)

if user_bet:
    race_on = True

while  race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won the bet, the {winning_color} turtle is winner")
            else:
                print(f"You lose the bet, the {winning_color} turtle is winner")
        steps = random.randint(1,10)
        turtle.forward(steps)



my_screen.exitonclick()