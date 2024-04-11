import turtle

# Create a turtle object
pen = turtle.Turtle()

# Set pen color and speed
pen.color("red")  # You can change the color as desired
pen.speed(1)  # Adjust speed as needed

# Function to draw a straight line
def draw_line(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)

# Starting position for the first letter
x_start = -100

# Draw letter D
draw_line(x_start, 50, x_start, -50)  # Vertical line
pen.penup()
pen.goto(x_start, 50)
pen.pendown()
pen.circle(-50, 180)  # Semi-circle

# Update x position for the next letter
x_start += 100  

# Draw letter N
draw_line(x_start, 50, x_start, -50)  # First vertical line
draw_line(x_start, 50, x_start + 100, -50)  # Diagonal line
draw_line(x_start + 100, 50, x_start + 100, -50)  # Second vertical line

# Update x position for the next letter
x_start += 150  # Adjust spacing as needed

# Draw letter T
draw_line(x_start, 50, x_start + 100, 50)  # Horizontal line
draw_line(x_start + 50, 50, x_start + 50, -50)  # Vertical line

# Hide the turtle
pen.hideturtle()

# Keep the window open until closed manually
turtle.done()
