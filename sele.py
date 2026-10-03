import turtle
from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=600, height=600)
screen.title("My turtle race")

y_pos = [-150, -50, 50, 150]
colors = ["red", "blue", "green", "purple"]

all_turtle = []

for index in range(4):
    tim = Turtle("turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-250, y=y_pos[index])
    random = randint(1, 30)
    all_turtle.append(tim)


is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        random_distance = randint(0, 2)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            print(f"The winner is the {winning_color} turtle!")



screen.exitonclick()
screen.mainloop()


