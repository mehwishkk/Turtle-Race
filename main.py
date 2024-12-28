from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the colour")
colors = ['red','orange','yellow','green','blue','purple']
all_turtles=[]
i=0
y=100
while i <6 :
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(-230, -y)
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)
    i=i+1
    y=y-30
is_race_on = True
while is_race_on == True:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet.lower() == winning_color.lower():
                print(f"You've won. The winner is {winning_color} turtle.")
            else:
                print(f"You lost. The winner is {winning_color} turtle.")
        random_dist= random.randint(0,10)
        turtle.forward(random_dist)

screen.exitonclick()
