# Second approach Turtle mini project shape 2
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
turtle.pensize(2) 



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

	equilateral(length)

	counter_1 = 1 
	while counter_1 < 4:

		turtle.penup()
		turtle.setposition(0,0)
		turtle.setposition(length * counter_1, - height * counter_1)
		turtle.pendown()
		equilateral(length)

		counter_1 += 1

	counter_2 = 1
	while counter_2 < 4:

		turtle.penup()		
		turtle.setposition(0,0)
		turtle.setposition(-length * counter_2, -height * counter_2)
		turtle.pendown()
		equilateral(length)

		counter_2 += 1

	counter_3 = -1
	while counter_3 < 2:

		turtle.penup()
		turtle.setposition(0,0)
		turtle.setposition(length * counter_3, - height * 3)
		turtle.pendown()
		equilateral(length)

		counter_3 += 2


l = 50 # => int
pattern(l)

# End filling.
turtle.end_fill() 

# To prevent the canvas to close automatically.
turtle.exitonclick() 