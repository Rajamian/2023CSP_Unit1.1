
import turtle as trtl
painter = trtl.Turtle()
painter.speed(10)
angle = 200
height = 10000
space = 100
color1 = "blue"
color2 = ("red")
painter.color(color1)

while painter.ycor() < height:
    if painter.pencolor() == color2:
        painter.fillcolor(color1)
        painter.color(color1)
    else:
        painter.fillcolor(color2)
        painter.color(color2)
    painter.right(angle)
    painter.forward(2 * space + 10) # experiment
    painter.begin_fill()
    painter.circle(3)
    painter.end_fill()
    space = space + 1
    if (space % 200 == 0):
        painter.fillcolor(color2)
        painter.color(color1)
    elif(space % 100 == 0):
        painter.fillcolor(color2)
        painter.color(color1)