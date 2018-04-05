# Fourth approach turtle mini project shape 3
import turtle

# Speed of the drawing (optional)
turtle.speed(1) # => NoneType

# Set the shape of the cursor
turtle.shape('turtle') # => NoneType

# Set the colort of the cursor and the drawing lines to blue
turtle.color('blue') # => NoneType

# Set line thickness (Optional)
turtle.pensize(2) # => NoneType


def k_c_shape(length):


	coordinates =[(0,2),(2,0),(0,2),(0,4),(0,2),(2,4),(5,4),(3,4),(3,0),(5,0)]

	for index, coordinate in enumerate(coordinates):

		if index == 6:

			# Cursor up
			turtle.penup() # => NoneType

			# Set position before continuing the shape
			turtle.setposition(length * 3, length * 4) # 

			# Cursor down
			turtle.pendown() # => NoneType

		turtle.setposition(length * coordinate[0], length * coordinate[1])

# Calling the k_c_shape function 
k_c_shape(60) # => NoneType

# To prevent the canvas to close automatically.
turtle.exitonclick() # => NoneType