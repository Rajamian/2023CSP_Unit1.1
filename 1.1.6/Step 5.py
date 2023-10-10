#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
Spider = trtl.Turtle()
Spider.pensize(40)
Spider.circle(20)
legs = 6
Lengthoflegs = 70
Space = 380 / legs
Spider.pensize(5)
n = 0
while (n < legs):
  Spider.goto(0, 0)
  Spider.setheading(Space * n)
  Spider.forward(Lengthoflegs)
  n = n + 1
Spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()