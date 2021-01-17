#Hoc lession : spiral
#Author : Anson

import turtle as t
from random import randint, random

def draw_star(size, points, x, y, color):
    angle = 180 - (180 / points)

    #define the color of the star
    t.color(color)

    t.penup()
    t.goto(x,y)
    t.pendown()

    t.begin_fill()

    #repeat
    for i in range(points):
        #draw line
        t.forward(size)
        # turn angle
        t.right(angle)

    
    # end filling the star
    t.end_fill()



t.Screen().bgcolor('dark blue')
t.speed(20)
#input()


while True:

    ranSize = randint(10,50)
    ranPits = randint(2,5) * 2 + 1

    ranX = randint(-500, 500)
    ranY = randint(-400, 400)

    ranColor = (random(), random(), random())
    
    draw_star(ranSize, ranPits, ranX, ranY, ranColor)
    
