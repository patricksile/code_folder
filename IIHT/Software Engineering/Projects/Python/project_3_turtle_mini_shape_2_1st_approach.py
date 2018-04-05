# First approach Turtle mini project shape 2
import turtle # turtle object
 
# Begin filling
turtle.begin_fill()
# Drawing speed (optional)
turtle.speed(0) 

# Cursor shape
turtle.shape('turtle') 
 
# Line and filling  colors
turtle.color('blue','green') 
 
# Line thickness (Optional)
turtle.pensize(2) 
 
 
def equilateral(lenght, angle):
 
    turtle.forward(lenght * 2) 
    turtle.left(angle)
    turtle.forward(lenght)
    turtle.left(angle)
    turtle.forward(lenght)
    turtle.right(angle)
    turtle.forward(lenght)
    turtle.right(angle)
    turtle.forward(lenght)
    turtle.left(angle)
    turtle.forward(lenght)
    turtle.left(angle)
    turtle.forward(lenght * 2)
    # Reset the initial position
    turtle.left(angle)
 
 
 
 
 
# lenght, angle and height
l,a = (50,120)
h = ((l * 2) ** 2 - (l ** 2)) ** 0.5

 
# calling the function
equilateral(l,a) # first green sets
 
turtle.penup()
turtle.setposition(0,0)
turtle.setposition(l, -h)
turtle.pendown()
 
equilateral(l,a) # second green sets
 
turtle.penup()
turtle.setposition(0,0)
turtle.setposition(-l, -h)
turtle.pendown()
 
equilateral(l,a) # third green sets
 
turtle.penup()
turtle.setposition(0,0)
turtle.setposition(-l * 2, -(h * 2))
turtle.pendown()
 
equilateral(l,a) # fourth green sets
 
turtle.penup()
turtle.setposition(0,0)
turtle.setposition(-(l * 3), -(h * 3))
turtle.pendown()
 
equilateral(l,a) # fifth green sets
 
turtle.penup()
turtle.setposition(0,0)
turtle.setposition(-l, -(h * 3))
turtle.pendown()
 
equilateral(l,a) # sixth green sets
 
turtle.penup()
turtle.setposition(0,0)
turtle.setposition(l, -(h * 3))
turtle.pendown()
 
equilateral(l,a) # seventh green sets
 
turtle.penup()
turtle.setposition(0,0)
turtle.setposition(l * 2, -h * 2)
turtle.pendown()
 
equilateral(l,a) # heighth green sets
 
turtle.penup()
turtle.setposition(0,0)
turtle.setposition(l * 3, -h * 3)
turtle.pendown()
 
equilateral(l,a) # nineth green sets
 
# End filling.
turtle.end_fill() 
 
# To prevent the canvas to close automatically.
turtle.exitonclick() 