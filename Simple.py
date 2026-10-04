from turtle import *
 
t = Turtle()
t.color('blue')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(3)

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def setKhaki():
    t.color('green')

def setYellow():
    t.color('yellow')

def setcircle():
    t.circle(50)

def stepRight():
    t.goto(t.xcor() + 5, t.ycor())

scr = t.getscreen()

scr.listen()
scr.onkey(stepRight, 'Right')

def stepLeft():
    t.goto(t.xcor() -5, t.ycor())

scr = t.getscreen()

scr.onkey(stepLeft, 'Left')

def stepUP():
    t.goto(t.xcor(), t.ycor() + 5)

scr = t.getscreen()

scr.listen()
scr.onkey(stepUP, 'UP')

def stepDOWN():
    t.goto(t.xcor(), t.ycor() - 5)

def
scr = t.getscreen()

scr.listen()
scr.onkey(stepDOWN, 'DOWN')

scr.onkey(setKhaki, 'k')

scr.onkey(setYellow,'y')

scr.onkey(setcircle, 'c')

scr.onscreenclick(move)
t.ondrag(draw)
