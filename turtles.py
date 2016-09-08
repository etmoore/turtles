import turtle

screen = turtle.Screen()
screen.bgcolor("orange")

def draw_square():

    sheldon = turtle.Turtle()
    sheldon.shape("classic")
    sheldon.color("green")
    sheldon.pensize(4)
    sheldon.speed(5)

    x = 0
    while x < 4:
        sheldon.forward(200)
        sheldon.right(90)
        x += 1

def draw_circle():
    carolyn = turtle.Turtle()
    carolyn.shape("turtle")
    carolyn.color("purple")
    carolyn.circle(150);


draw_square()
draw_circle()
screen.exitonclick()

