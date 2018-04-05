# Fourth approach Turtle mini project shape 2

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
	turtle.forward(lenght * 2) # => NoneType
	
	# angles angle direction
	angle_direction = [1,-1, 1] # Changes angle_direction of turtle.left() or turtle.right()
	for direction in angle_direction:

		turtle.left(direction * 120)
		turtle.forward(lenght)
		turtle.left(direction * 120)
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

	# Coordinate points.
	coordinates = [(1,-1),(2,-2),(3,-3),(-1,-1),
	(-2,-2),(-3,-3),(-1,-3),(1,-3)] # => list

	for i in range(8):
		
		turtle.penup()
		turtle.setposition(0,0)
		turtle.setposition(length * coordinates[i][0], height * coordinates[i][1])
		turtle.pendown()
		equilateral(length)



# Calling the function
l = 50
pattern(l)

# End filling.
turtle.end_fill() # => NoneType

# To prevent the canvas to close automatically.
turtle.exitonclick() # => NoneType