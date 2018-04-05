# Third approach Turtle mini project shape 2
import turtle # turtle object

# Begin filling
turtle.begin_fill()
# Drawing speed (optional)
turtle.speed(10)

# Cursor shape
turtle.shape('turtle') 

# Line and filling  colors
turtle.color('blue','green') 

# Line thickness (Optional)
turtle.pensize(1) 



def equilateral(lenght):

	"""
		This function draws a pattern of three green triangle.
	"""
	# First line
	turtle.forward(lenght * 2) 
	
	# angles direction
	direction = [1,-1, 1] # Changes direction of turtle.left() or turtle.right()
	for i in direction:

		turtle.left(i * 120)
		turtle.forward(lenght)
		turtle.left(i * 120)
		turtle.forward(lenght)

	# Last line
	turtle.forward(lenght)

	# Reset the initial position
	turtle.left(120)

def pattern(length):

	"""
		This fuction repeats the equilateral function by coordinates.
	"""
	# Calculate the height of the triangle
	height = ((length * 2) ** 2 - length ** 2) ** 0.5 # => int

	equilateral(length) # First equilateral green pattern

	for i in range(1, 4):
		
		turtle.penup()
		turtle.setposition(0,0)
		turtle.setposition(length * i, - height * i)
		turtle.pendown()
		equilateral(length)

	for i in range(1, 4):

		turtle.penup()
		turtle.setposition(0,0)
		turtle.setposition(-length * i, - height * i)
		turtle.pendown()
		equilateral(length)	

	for i in range(-1, 2, 2):

		turtle.penup()
		turtle.setposition(0,0)
		turtle.setposition(length * i, - height * 3)
		turtle.pendown()
		equilateral(length)		


l = 50 # => int

pattern(l)

# End filling.
turtle.end_fill() 

# To prevent the canvas to close automatically.
turtle.exitonclick() 