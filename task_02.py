import turtle  # Import the turtle graphics module
import math  # Import the math module for mathematical functions

# Function to draw the Pythagoras tree
def draw_pythagoras_tree(order, size, angle=45):
    if order == 0:
        turtle.forward(size)  # Draw the branch
        turtle.backward(size)  # Move back to the original position
    else:
        turtle.pensize(2)  # Set the pen size
        turtle.pencolor("#a62c2c")  # Set the pen color
        turtle.fillcolor("#f6eaea")  # Set the fill color
        turtle.begin_fill()  # Begin filling the shape
        turtle.forward(size)  # Draw the branch
        turtle.left(angle)  # Turn left by the given angle
        draw_pythagoras_tree(order - 1, size * math.cos(math.radians(angle)), angle)  # Recursive call to draw the left subtree
        turtle.right(2 * angle)  # Turn right by twice the given angle
        draw_pythagoras_tree(order - 1, size * math.cos(math.radians(angle)), angle)  # Recursive call to draw the right subtree
        turtle.left(angle)  # Turn left by the given angle to return to the original orientation
        turtle.backward(size)  # Move back to the original position
        turtle.end_fill()  # End filling the shape

if __name__ == "__main__":
   # Initialize turtle
   turtle.speed(0)  # Set the drawing speed to the maximum
   turtle.left(90)  # Point the turtle upwards

   screen = turtle.Screen()  # Create a screen object
   screen.title("Pythagoras Tree")  # Set the title of the window

   # Get the recursion level from the user
   level = int(input("Enter the recursion level (integer): "))  # Input the recursion level from the user
   size = 100  # Set the initial size of the tree

   # Draw the Pythagoras tree
   draw_pythagoras_tree(level, size)  # Call the function to draw the tree

   # Finish turtle drawing
   turtle.done()  # Finish the turtle drawing
