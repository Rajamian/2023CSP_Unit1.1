#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

color1 = "red"

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 100 # the radius of the circle
angle = 90 # experiment
seg = int(360/angle) # the length of a line

# Add a loop with a zero-iteration condition
start_loop = 'y'

while (start_loop == 'y'):
    painter.right(angle)
    painter.forward(space)
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()

# Add an infinite loop

wn = trtl.Screen()
wn.mainloop()