# Fifth approach Turtle mini project shape 2

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


def equilateral(length, index):

	"""
		This function draws a pattern of three green triangle.
	"""
	# Height calculation (Pythagore theorem)
	height = ((length * 2) ** 2 - length ** 2) ** 0.5 # => int
	
	# First line
	turtle.forward(length * 2) 
	
	# angles angle direction
	angle_direction = [1,-1, 1] # Changes angle_direction of turtle.left() or turtle.right()
	for direction in angle_direction:

		turtle.left(direction * 120)
		turtle.forward(length)
		turtle.left(direction * 120)
		turtle.forward(length)

	# Last line
	turtle.forward(length)

	# Reset the initial position
	turtle.left(120)

	if index < 8:
		# Coordinates points.
		coordinates = [(1,-1),(2,-2),(3,-3),(-1,-1),
		(-2,-2),(-3,-3),(-1,-3),(1,-3)]

		turtle.penup()
		turtle.setposition(0,0)
		turtle.setposition(length * coordinates[index][0], height * coordinates[index][1])
		turtle.pendown()

		return equilateral(length, index + 1)



# Calling the function
l = 50	# => int
i = 0	# => int
equilateral(l,i)

# End filling.
turtle.end_fill() 

# To prevent the canvas to close automatically.
turtle.exitonclick() 