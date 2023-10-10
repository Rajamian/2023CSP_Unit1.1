#   Add your code here and add comments to your code
#   to describe what each section of code is doing

# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle
painter.circle(50, 360)

# move the turtle to another part of the screen
painter.penup()
painter.goto(0, -0)
painter.pendown()

# add code here for an arc
painter.circle(-75, 360)

# move the turtle to another part of the screen
painter.penup()
painter.goto(0, -150)
painter.pendown()

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.circle(-100, 360)

# move the turtle to another part of the screen
painter.penup()
painter.goto(0, 100)
painter.pendown()
# add code here to create a polygon of your choice using the circle method
painter.pencolor("red")
painter.fillcolor("blue")
painter.begin_fill()
painter.circle(25, 360, 4)
painter.end_fill()


# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()