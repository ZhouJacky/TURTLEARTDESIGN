def snowflake(t,x,y):
    t.speed(0)
    t.color('white')
    t.width(4)
    t.circle(25,360)

    a=45

    for times in range(8):
        t.circle(25,a)
        t.right(90)
        t.forward(100)
        t.backward(50)
        t.left(45)
        t.forward(30)
        t.backward(30)
        t.right(90)
        t.forward(30)
        t.backward(30)
        t.left(45)
        t.backward(50)
        t.left(90)
        

    t.penup()    
    t.goto(x,y)
    t.pendown()

def star(t, dist,x,y):
    t.speed(0)
    for times in range(5):
        t.forward(dist)
        t.left(144)

    t.penup()    
    t.goto(x,y)
    t.pendown()



        




