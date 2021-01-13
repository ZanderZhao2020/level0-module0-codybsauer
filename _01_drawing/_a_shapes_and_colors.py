import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    coolTurtle = turtle.Turtle()
    
    # Make your turtle's shape 'turtle', .shape('turtle')
    coolTurtle.shape('turtle')

    # Set your turtle's speed using .speed(2)
    coolTurtle.speed(2)
    
    # Set your turtle's color using .color('green') and .pencolor('blue')
    coolTurtle.color('green')
    coolTurtle.pencolor('blue')
    
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)

    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    coolTurtle.begin_fill()
    for i in range(4):
        coolTurtle.forward(100)
        coolTurtle.left(90)

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    # coolTurtle.goto(-50, 0)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?

    coolTurtle.color('blue')
    coolTurtle.circle(50, 360)
    coolTurtle.end_fill()
    
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!

    coolTurtle.begin_fill()
    coolTurtle.color('orange')

    for i in range(5):
        coolTurtle.forward(100)
        coolTurtle.right(360 / 5)

    coolTurtle.end_fill()

    coolTurtle.begin_fill()
    coolTurtle.color('red')

    for i in range(3):
        coolTurtle.forward(100)
        coolTurtle.right(120)

    coolTurtle.end_fill()

    coolTurtle.penup()
    coolTurtle.goto(50, 50)
    coolTurtle.pendown()

    coolTurtle.begin_fill()
    coolTurtle.color('purple')

    for i in range(6):
        coolTurtle.forward(100)
        coolTurtle.left(360/6)

    coolTurtle.end_fill()

    # coolTurtle.penup()


# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
