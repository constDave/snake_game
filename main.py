from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = []
x_axis = 0

square = Turtle()

square.shape("square")
square.color("white")
square.penup()

for _ in range(3):
    snake.append(square)

for square in snake:
    square.goto(x=x_axis, y=0)
    x_axis -= 20
    square.stamp()


screen.exitonclick()