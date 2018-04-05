# First approach turtle mini object shape 3
import turtle

# Speed of the drawing (optional)
turtle.speed(1) # => NoneType

# Set the shape of the cursor
turtle.shape('turtle') # => NoneType

# Set the colort of the cursor and the drawing lines to blue
turtle.color('blue') # => NoneType

# Set line thickness (Optional)
turtle.pensize(2) # => NoneType

# Draw the shape K

#====================== Start of shape K ==========================

turtle.setposition(0,100) # => NoneType
turtle.setposition(100,0) # => NoneType
turtle.setposition(0,100) # => NoneType


turtle.setposition(0,200) # => NoneType
turtle.setposition(0,100) # => NoneType
turtle.setposition(100,200) # => NoneType


#====================== End of shape K ==========================

# Cursor up
turtle.penup() # => NoneType

# Set position before continuing the shape
turtle.setposition(150, 200) # 

# Cursor down
turtle.pendown() # => NoneType

#====================== Start of shape C ==========================

turtle.setposition(250,200) # => NoneType
turtle.setposition(150,200) # => NoneType
turtle.setposition(150,0) # => NoneType
turtle.setposition(250,0) # => NoneType


#====================== End of shape C ==========================

# To prevent the canvas to close automatically.
turtle.exitonclick() # => NoneType