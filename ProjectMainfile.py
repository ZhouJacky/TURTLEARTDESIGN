import turtle
import random
from snow import*

turtle.bgcolor('cyan')
bob=turtle.Turtle()
bob.speed(0)



for times in range(10):
    x=random.randint(-800,800)
    y=random.randint(-500,500)
    snowflake(bob,x,y)

for times in range(20):
    x=random.randint(-800,800)
    y=random.randint(-500,500)
    star(bob,50,x,y)
