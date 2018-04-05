# /usr/bin/env python3.5
import turtle  # turtle object

# Speed of the drawing (optional)
# turtle.speed(10) # => NoneType

# Set the shape of the cursor
turtle.shape('turtle') # => NoneType

# Set the color of the cursor and the drawing lines to blue
turtle.color('blue') # => NoneType

# Set line thickness (Optional)
turtle.pensize(1) # => NoneType

# Initialize rotation angle
rotation_angle = 10 # => int

# first counter
counter_1 = 0 # => int

while counter_1 < 360 / rotation_angle: # while loop

#====================== Start of lozenge drawing ==========================

	# lozenge angles
	lozenge_angles = [50,130, 50, 130 + rotation_angle] # => list

	for corner_angle in lozenge_angles:

		# 100 pixels forward
		turtle.forward(50) # => NoneType

		# 40 degree clockwise
		turtle.right(corner_angle) # => NoneType	

#====================== End of lozenge drawing ==========================

	# first counter incremetation
	counter_1 += 1 # => int



#====================== Start of of the out coming line ==========================

# Set the cursor 90 degree south
turtle.right(90) # => NoneType

# Move cursor out of the main shape
turtle.forward(150) # => NoneType

#====================== End of of the out coming line ==========================


# To prevent the canvas to close automatically.
turtle.exitonclick() # => NoneType
