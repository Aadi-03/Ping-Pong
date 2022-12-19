import turtle
import random
turtle.bgcolor("black")

winner=turtle.Turtle()
winner.pencolor("white")
winner.hideturtle()


playera = 0
playerb = 0
tw =  turtle.Turtle()
tw.speed(0)
tw.pencolor("white")
tw.penup()
tw.hideturtle()
tw.goto(0,300)
tw.write("Player A :{}    Player B : {}".format(playera,playerb) ,align="center",font= ("arial",28))

    
t1 = turtle.Turtle()
t2 = turtle.Turtle()
ts = turtle.Turtle()
tb = turtle.Turtle()

t1.pencolor("white")
t2.pencolor("white")
ts.pencolor("white")
tb.pencolor("white")

t1.speed(0)
t2.speed(0)
ts.speed(0)
tb.speed(0)

t1.up()
t1.goto(-300,0)
t2.up()
t2.goto(300,0)
ts.up()
ts.goto(-320,300)
ts.down()

#square (boundary)
ts.fd(640)
ts.right(90)
ts.fd(610)
ts.right(90)
ts.fd(640)
ts.right(90)
ts.fd(610)
ts.hideturtle()



t1.left(90)
t2.left(90)    
t1.shape("square")
t1.fillcolor("white")
t1.shapesize(1,4),
t2.shape("square")
t2.fillcolor("white")
t2.shapesize(1,4)
tb.shape("circle")
tb.fillcolor("red")
tb.penup()

def t1moveup():
    while t1.ycor() < 260:
        n1 = t1.ycor()
        
        n1+=20
        t1.goto(-300,n1)
        break
turtle.onkeypress(t1moveup,"w")
turtle.listen()
def t1movedown():
    while t1.ycor() > -255:
        n1 = t1.ycor()
        n1-=20
        t1.goto(-300,n1)
        break
turtle.onkeypress(t1movedown,"s")
turtle.listen()
def t2moveup():
    while t2.ycor() < 260:
        n1 = t2.ycor()
        
        n1+=20
        t2.goto(300,n1)
        break
turtle.onkeypress(t2moveup,"Up")
turtle.listen()
def t2movedown():
    while t2.ycor() > -255:
        n1 = t2.ycor()
        n1-=20
        t2.goto(300,n1)
        break
turtle.onkeypress(t2movedown,"Down")
turtle.listen()
x = 1.1
y = 0.95
#ball movments
while True:

    tb.setx(tb.xcor()+x)
    tb.sety(tb.ycor()+y)
    if tb.ycor() > 300:
        tb.sety(300)
        y*=-1
    if tb.ycor() < -300:
        tb.sety(-300)
        y*=-1
    if tb.xcor() > 310:
        tb.goto(0,0)
        x *=-1
        playera+=1
        tw.clear()
        tw.write("Player A : {}   Player B : {}" .format(playera,playerb),align="center",font= ("arial",28))
        if playera == 5:
            winner.write("player A has won",font=("arial",24))
            break
        elif playerb == 5:
            winner.write("player B has won",font=("arial",24))
            break            
        
    if tb.xcor() < -310:
        tb.goto(0,0)
        x *=-1
        playerb+=1
        tw.clear()
        tw.write("Player A : {}   Player B : {}" .format(playera,playerb),align="center",font= ("arial",28))
        if playera == 5:
            winner.write("player A has won",font=("arial",24))
            break
        elif playerb == 5:
            winner.write("player B has won",font=("arial",24))
     #collision with the paddle
    if (tb.xcor() > 290 and tb.ycor()<300) and (tb.ycor() < t2.ycor() + 60 and tb.ycor() > t2.ycor() - 60):
        tb.setx(290)
        x *=-2.5
        if x > 4:
            x=6
    if (tb.xcor() < -290 and tb.ycor()>-300) and (tb.ycor() < t1.ycor() + 60 and tb.ycor() > t1.ycor() - 60):
        tb.setx(-290)
        x *=-1.5
        if x > 4:
            x=6
