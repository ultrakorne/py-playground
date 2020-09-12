import turtle
import random


def draw_leg(scale):
    turtle.left(90)
    turtle.forward(30 * scale)
    turtle.left(90)
    turtle.forward(15 * scale)
    turtle.right(90)
    turtle.forward(10 * scale)
    turtle.right(90)
    turtle.forward(30 * scale)
    turtle.right(85)
    turtle.forward(45 * scale)
    turtle.left(85)


def draw_two_legs(scale):
    draw_leg(scale)
    turtle.forward(7 * scale)
    draw_leg(scale)


def draw_long_dog(length, scale, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(float(length) * scale)
    turtle.left(45)
    turtle.forward(35 * scale)
    turtle.right(45)
    turtle.forward(35 * scale)
    turtle.right(40)
    turtle.forward(25 * scale)
    turtle.left(40)
    turtle.forward(45 * scale)
    turtle.right(110)
    turtle.forward(25 * scale)
    turtle.right(70)
    turtle.forward(40 * scale)
    turtle.left(45)
    turtle.forward(90 * scale)
    turtle.right(45)
    turtle.forward(25 * scale)
    draw_two_legs(scale)
    turtle.forward(float(length) * scale * 0.65)
    draw_two_legs(scale)
    turtle.right(85)
    turtle.forward(45 * scale)
    turtle.goto(x, y)
    turtle.setheading(0)


def click(x, y):
    print(f"{x} {y}")
    turtle.color(random.random(), random.random(), random.random())
    draw_long_dog(500, 0.5, x, y)


turtle.color(1, 0, 0)
turtle.pensize(2)
turtle.speed(0)
draw_long_dog(500, 1, -500, 500)
turtle.color(0, 1, 0)
draw_long_dog(500, 0.5, -500, -100)

# for i in range(10):
#     draw_long_dog(500, 0.5, 0, 0)
#     turtle.right(15 * i)

turtle.onscreenclick(click)
turtle.done()
