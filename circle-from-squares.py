import turtle

# draw a square
# turn to the right a few degrees
# repeat many times
screen = turtle.Screen()
zach = turtle.Turtle()
zach.speed(7)

def draw_square(turtle):
    for i in range(0,4):
        turtle.forward(150)
        turtle.right(90)

for i in range (0,360):
    draw_square(zach)
    zach.right(1)

screen.exitonclick()
