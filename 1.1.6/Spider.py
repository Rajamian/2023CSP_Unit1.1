#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
Spider = trtl.Turtle()
#Create the body of a spider
Spider.pensize(40)
Spider.circle(20)
#Configure the Legs
Spider.pencolor("black")
legs = 8
Lengthoflegs = 70
Angle = 360 / legs - 20
Spider.pensize(5)
n = 0
#Draw the legs
while (n < legs):
  if(n<4):
    Spider.goto(0, 25)
    Spider.setheading(Angle * n - 45)
    Spider.forward(Lengthoflegs)
  else:
    Spider.goto(0, 25)
    Spider.setheading(Angle * n + 45)
    Spider.forward(Lengthoflegs)
  n = n + 1

#Draw eyes
Spider.penup()
Spider.goto(10, 5)
Spider.pendown()
Spider.pencolor("red")
Spider.pensize(5)
Spider.circle(2)
Spider.penup()
Spider.goto(-10, 5)
Spider.pendown()
Spider.pencolor("red")
Spider.pensize(5)
Spider.circle(2)

Spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()