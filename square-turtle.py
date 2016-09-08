import turtle

def draw_square():
    screen = turtle.Screen()
    screen.bgcolor("orange")

    sheldon = turtle.Turtle()
    sheldon.shape("classic")
    sheldon.color("green")
    sheldon.pensize(4)
    sheldon.speed(5)

    sheldon.forward(200)
    sheldon.right(90)

    sheldon.forward(200)
    sheldon.right(90)

    sheldon.forward(200)
    sheldon.right(90)

    sheldon.forward(200)
    sheldon.right(90)

    screen.exitonclick()

draw_square()
