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

def draw_triangle():
    george = turtle.Turtle()
    george.shape("arrow")
    george.color("blue")

    x = 0
    while x < 3:
        george.forward(150)
        george.left(120)
        x += 1

draw_square()
draw_circle()
draw_triangle()
screen.exitonclick()

