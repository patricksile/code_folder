# /usr/bin/env python3.5
import turtle  # turtle object
import math
# Speed of the drawing (optional)
# turtle.speed(10) # => NoneType

# Set the shape of the cursor
turtle.shape('turtle') # => NoneType

# Set the color of the cursor and the drawing lines to blue
turtle.color('blue') # => NoneType

# Set line thickness (Optional)
turtle.pensize(2) # => NoneType


# Lozenge side
l_side = 100
# Initialize rotation angle
rotation_angle = math.radians(10) # => int

# Some angles I am manipulating so far
accute_angle = math.radians(30 + rotation_angle * 0)

# Some cos and sin manipulations
cosine = math.cos(accute_angle)
sine = math.sin(accute_angle)
sine_rotation = math.sin(rotation_angle * 0)
cosine_rotation = math.cos(rotation_angle * 0)
# Some external sides

opposite_side = sine * l_side
adjacent_side = cosine * l_side
opposite_rotation_side = sine_rotation * l_side
adjacent_rotation_side = cosine_rotation * l_side


# Using only the goto method but it makes it more tricky

# First lozenge
turtle.goto(l_side, opposite_rotation_side)

turtle.goto(l_side + adjacent_side, opposite_side)

turtle.goto(adjacent_side, opposite_side)

turtle.goto(0,0)





accute_angle = math.radians(30 + rotation_angle * 1)

# Some cos and sin manipulations
cosine = math.cos(accute_angle)
sine = math.sin(accute_angle)

sine_rotation = math.sin(rotation_angle * 1)
cosine_rotation = math.cos(rotation_angle * 1)
# Some external sides

opposite_side = sine * l_side
adjacent_side = cosine * l_side
opposite_rotation_side = sine_rotation * l_side
adjacent_rotation_side = cosine_rotation * l_side


# Using only the goto method but it makes it more tricky
# Second lozenge
turtle.goto(adjacent_rotation_side , opposite_rotation_side)

turtle.goto(adjacent_rotation_side + adjacent_side, opposite_rotation_side + opposite_side)

turtle.goto(adjacent_side, opposite_side)

turtle.goto(0,0)



# accute_angle = math.radians(30 + rotation_angle * 2)

# # Some cos and sin manipulations
# cosine = math.cos(accute_angle)
# sine = math.sin(accute_angle)

# sine_rotation = math.sin(rotation_angle * 2)
# cosine_rotation = math.cos(rotation_angle * 2)
# # Some external sides

# opposite_side = sine * l_side
# adjacent_side = cosine * l_side
# opposite_rotation_side = sine_rotation * l_side
# adjacent_rotation_side = cosine_rotation * l_side

# # Using only the goto method but it makes it more tricky
# # Third lozenge

# turtle.goto(adjacent_rotation_side, opposite_rotation_side)

# turtle.goto(adjacent_rotation_side + adjacent_side, opposite_rotation_side + opposite_side)

# turtle.goto(opposite_rotation_side, adjacent_rotation_side)

# turtle.goto(0,0)

# (l_side ** 2) - (l_side * sine / 2) ** 2
# first counter
# counter_1 = 0 # => int

# while counter_1 < 360 / rotation_angle: # while loop

#====================== Start of lozenge drawing ==========================

	# lozenge angles
	# lozenge_angles = [50,130, 50, 130 + rotation_angle] # => list

	# for corner_angle in lozenge_angles:

		# 100 pixels forward
		# turtle.forward(50) # => NoneType

		# 40 degree clockwise
		# turtle.right(corner_angle) # => NoneType	

#====================== End of lozenge drawing ==========================

	# first counter incremetation
	# counter_1 += 1 # => int



#====================== Start of of the out coming line ==========================

# Set the cursor 90 degree south
# turtle.right(90) # => NoneType

# Move cursor out of the main shape
# turtle.forward(150) # => NoneType

#====================== End of of the out coming line ==========================


# To prevent the canvas to close automatically.
turtle.exitonclick() # => NoneType
