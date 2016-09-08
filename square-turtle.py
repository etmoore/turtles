import turtle

def draw_square():
    screen = turtle.Screen()
    screen.bgcolor("orange")

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

    screen.exitonclick()

draw_square()
