
import time
from random import randint
from turtle import *

# window Setup

win=Screen()
win.title("Turtle Race")
bgcolor("lightgreen")
speed(0)
penup()
setpos(-150,200)
write("TURTLE RACE",font=('Comic Sans MS',30,'bold'))  # title

s1=Turtle()
s1.penup()
s1.shape('square')

s2 = Turtle()
s2.penup()
s2.shape('square')

s1.color('tomato')
s1.shapesize(0.5)
s2.shapesize(0.5)

'''def dirt(x,y):
    setpos(x,y)
    color("lightblue")
    begin_fill()
    pendown()
    for i in range(2):
        forward(800)
        right(90)
        forward(200)
        right(90)
    end_fill()

dirt(-400,-250)
dirt(-400,450)'''

# race track

def track(x,y):
    setpos(x,y)
    color("black")
    begin_fill()
    pendown()
    for i in range(2):
        forward(800)
        right(90)
        forward(200)
        right(90)
    end_fill()

track(-400,150)
track(-400,10)


# boarder line

penup()
def border(obj1,obj2,y):
    for i in range(0,155,15):
        j=0
        while j<6:
            obj1.setpos((i+j)*5+(-400),y)
            obj1.speed(0)
            obj1.stamp()
            obj2.setpos((i+1.5 + j) * 5 + (-370), y)
            obj2.stamp()
            obj2.speed(0)
            j+=1

border(s1,s2,160)
border(s1,s2,-200)

# Finish line

s1.color("white")
s2.color("black")
s1.shapesize(1)
s2.shapesize(1)
s1.speed(0)
s2.speed(0)
def line(obj1,obj2,x):
    for i in range(1,20,2):
        penup()
        obj1.setpos(300+x,i*(-20)+(190))
        obj2.setpos(300+x, (i+1)*(-20)+ (190))
        pendown()
        obj1.stamp()
        obj2.stamp()
line(s1,s2,0)
line(s2,s1,20)

# title continue
s1.penup()
s1.shape('turtle')
s1.color('green')
s1.shapesize(2)
s1.setpos(150,220)
s1.left(90)
s1.pendown()

# Race
red = Turtle()
red.color('red')
red.shape('turtle')
red.penup()
red.goto(-300,100)
red.pendown()
red.right(360)

orange = Turtle()
orange.color('orange')
orange.shape('turtle')
orange.penup()
orange.goto(-300,60)
orange.pendown()
orange.right(360)

green = Turtle()
green.color('green')
green.shape('turtle')
green.penup()
green.goto(-300,20)
green.pendown()
green.right(360)

magenta = Turtle()
magenta.color('magenta')
magenta.shape('turtle')
magenta.penup()
magenta.goto(-300,-20)
magenta.pendown()
magenta.right(360)

skyblue = Turtle()
skyblue.color('skyblue')
skyblue.shape('turtle')
skyblue.penup()
skyblue.goto(-300,-60)
skyblue.pendown()
skyblue.right(360)

maroon = Turtle()
maroon.color('maroon')
maroon.shape('turtle')
maroon.penup()
maroon.goto(-300,-100)
maroon.pendown()
maroon.right(360)

cyan = Turtle()
cyan.color('cyan')
cyan.shape('turtle')
cyan.penup()
cyan.goto(-300,-140)
cyan.pendown()
cyan.right(360)

for turn in range(80):

    red.forward(randint(5,10))
    orange.forward(randint(5,10))
    green.forward(randint(5,10))
    magenta.forward(randint(5,10))
    skyblue.forward(randint(5,10))
    cyan.forward(randint(5,10))
    maroon.forward(randint(5, 10))

# rancking

finals_list = [red.xcor(),orange.xcor(),green.xcor(),magenta.xcor(),skyblue.xcor(),cyan.xcor(),maroon.xcor()]
finals_dict = {red.xcor():'Red',orange.xcor():'Orange',green.xcor():'Green',magenta.xcor():'Magenta',skyblue.xcor():'skyblue',cyan.xcor():'Cyan',maroon.xcor():'Maroom'}


finals_list = sorted(finals_list,reverse=True)

color('black')
penup()
setposition(-50,-250)
pendown()
pensize(2)
write('Ranking Board',align='left', font=('Arial',12,'bold'))
penup()
# 1st
setposition(-80,-280)
rank = finals_list[0]
pensize(2)
pendown()
write(f'1st place: {finals_dict[rank]} turtle',align='left',font=('Arial',12,'bold'))
hideturtle()


time.sleep(4)