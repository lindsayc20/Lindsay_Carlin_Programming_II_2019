
#Turtle Recursion (25pts)

#1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (10pts)  

import turtle
from math import pow

my_turtle = turtle.Turtle()  # create a turtle object
my_screen = turtle.Screen()  # create a screen object

my_turtle.width(4)
my_turtle.speed(-100)
my_turtle.shape("turtle")

my_turtle.penup()
my_turtle.pendown()
my_turtle.goto(0, 0)
my_turtle.setheading(180)
'''
def draw_h(length, depth):

    if depth > 0:
        my_turtle.forward(length / 2)
        my_turtle.right(90)
        my_turtle.forward(length / 2)
        my_turtle.left(90)

        draw_h(length / 2, depth - 1)

        my_turtle.left(90)
        my_turtle.forward(length)
        my_turtle.right(90)

        draw_h(length / 2, depth - 1)

        my_turtle.right(90)
        my_turtle.forward(length / 2)
        my_turtle.right(90)
        my_turtle.forward(length)
        my_turtle.left(90)
        my_turtle.forward(length / 2)
        my_turtle.left(90)

        draw_h(length / 2, depth - 1)

        my_turtle.left(90)
        my_turtle.forward(length)
        my_turtle.right(90)

        draw_h(length / 2, depth - 1)

        my_turtle.right(90)
        my_turtle.forward(length / 2)
        my_turtle.left(90)
        my_turtle.forward(length / 2)

draw_h(250, 5)

'''
#2)  Using the turtle library, create any of the other recursive patterns in the data folder. 
#  Challenge yourself to match your pattern as closely as you can to the image.  (10pts)
#  Note:  The Koch snowflake shows step by step building of the fractal.  
#  The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)

my_screen.clear()
my_turtle.penup()
my_turtle.goto(200, -200)
my_turtle.pendown()

def draw_fractal(length, depth):

    if depth > 0:
        my_turtle.forward(length)
        my_turtle.right(90)
        my_turtle.forward(length)
        my_turtle.right(90)
        my_turtle.forward(length)
        my_turtle.right(90)
        my_turtle.forward(length)
        my_turtle.right(90)
        my_turtle.forward(length / 2)
        my_turtle.right(45)
        draw_fractal(length / pow(2, 1/2), depth - 1)

draw_fractal(400, 10)

#3)  Create your own work of recursive art with a repeating pattern of your making (or choose another one from the files).  
#  It must be a repeated pattern using recursion (not just loops). Snowflakes, trees, and spirals are a common choice.  
#  Play around and have fun with it.  (5pt)

my_screen.clear()
my_turtle.penup()
my_turtle.goto(-100, -200)
my_turtle.pendown()
my_turtle.setheading(120)

def draw_spiral(length, depth):

    if depth > 0:
        my_turtle.forward(length)
        my_turtle.right(60)
        my_turtle.forward(length)
        my_turtle.right(60)
        my_turtle.forward(length)
        my_turtle.right(60)
        my_turtle.forward(length)
        my_turtle.right(60)
        my_turtle.forward(length)
        my_turtle.right(60)
        my_turtle.forward(length / 4)
        draw_spiral(length / 2, depth - 1)

draw_spiral(250, 10)
my_screen.exitonclick()

#  General expectations for all problems
#  Give all your fractals a depth of at least 4.  (Don't make programs that take forever though)  
#  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
#  All three recursive drawings can be on the same program.  Just use screen.clear() between problems.  Alternately, you could draw to three different screen objects.
#  Run your turtles at max speed.
#  Have fun!
 
#  Resource to help you out >>> https://docs.python.org/3.3/library/turtle