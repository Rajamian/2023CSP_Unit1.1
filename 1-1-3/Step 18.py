#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -200
y = -100

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    painter.color("gray")
    rem = floor % 6
if (rem < 2):
    #draw the floor
    painter.color("blue")

if (rem > 3):
    painter.color(lime)

wn = trtl.Screen()
wn.mainloop()