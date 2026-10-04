from turtle import *
from time import sleep
from random import randint

t = Turtle()
t.color('red')
t.penup()
t.shape('turtle')
t.speed(10)

t.points = 0

w = 200
h = 200

def rand_move(): 
    t.goto(randint(-w,w), randint(-h,h))
    
def catch(x, y): 
    t.write('A!',font=('Arial', 14, 'norwal'))
    t.points +=1
    rand_move()
t.onclick(catch)

while t.points < 3:
    sleep(1.5)
    rand_move()
t.write('WOW!',font=('Arial', 16,'bold'))
t.hideturtle()
