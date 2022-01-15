import turtle
from random import randint
if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    # This code makes a new Turtle. Pick a new name for the turtle
    Bob = turtle.Turtle()
    # Make your turtle's shape 'turtle', .shape('turtle')
    Bob.shape("turtle")
    # Set your turtle's speed using .speed(2)
    Bob.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Bob.color("green")
    Bob.pencolor("blue")
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    Bob.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    Bob.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for X in range(3):
        Bob.forward(100)
        Bob.left(90)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    # cool_turtle.goto(-50, 0)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    Bob.goto(-50, 0)
    Bob.begin_fill()
    Bob.circle(25, steps=30)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    Bob.end_fill()
    # Draw 3 more shapes with different fill colors!
    Bob.goto(-50, -50)
    Bob.stamp()
    Bob.goto(-50, -50)
    Bob.begin_fill()
    Bob.circle(45, steps=3)
    Bob.end_fill()
    Bob.speed(0)
    for X in range(500):
        Bob.goto(randint(-500, 501), randint(-500, 501))
    # cool_turtle.penup()
    Bob.penup()

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
