# Third approach turtle mini object shape 3
import turtle

# Speed of the drawing (optional)
turtle.speed(1) # => NoneType

# Set the shape of the cursor
turtle.shape('turtle') # => NoneType

# Set the colort of the cursor and the drawing lines to blue
turtle.color('blue') # => NoneType

# Set line thickness (Optional)
turtle.pensize(2) # => NoneType


def k_c_shape():


	coordinates = [(0,100),(100,0),(0,100),(0,200),(0,100),(100,200),(250,200),(150,200),(150,0),(250,0)]

	for index, coordinate in enumerate(coordinates):

		if index == 6:

			# Cursor up
			turtle.penup() # => NoneType

			# Set position before continuing the shape
			turtle.setposition(150, 200) # 

			# Cursor down
			turtle.pendown() # => NoneType

		turtle.setposition(coordinate)

k_c_shape() # => NoneType
# To prevent the canvas to close automatically.
turtle.exitonclick() # => NoneType