import turtle
#score
score_A=0
score_B =0
#screen
win= turtle.Screen() 
win.setup(800,600)
win.bgcolor("black")
win.title("Pong Game")
win.tracer(0)

#LEFT PADDLE:
left_paddle=turtle.Turtle()
left_paddle.speed(10)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.penup()
left_paddle.goto(-380,0)


#RIGHT PADDLE:
right_paddle=turtle.Turtle()
right_paddle.speed(10)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(380,0)


#BALL:
ball=turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.speed(0)
ball.dx=1
ball.dy=1
ball.penup()
#score
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0    Player B : 0",align="center",font=("Sans Serif",24,"normal"))


#MOVING PADDLE:
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)
def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)
def right_paddle_down():
    right_paddle.sety(right_paddle.ycor()-20)


win.listen()
win.onkeypress(left_paddle_up, 'w')
win.onkeypress(left_paddle_down, 's')
win.onkeypress(right_paddle_up, 'Up')
win.onkeypress(right_paddle_down, 'Down')

while True:
    win.update()
    #BALL MOVEMENT
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #ball-wall collision
    #top wall
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    #bottom wall    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    #right wall    
    if ball.xcor()>385:
        ball.setx(385)
        ball.dx *= -1
        score_A+=1
        pen.clear()
        pen.write("Player A : {}    Player B : {}".format(score_A,score_B),align="center",font=("Sans Serif",24,"normal"))
    #left wall    
    if ball.xcor()<-385: 
        ball.setx(-385)
        ball.dx *= -1
        score_B+=1
        pen.clear()
        pen.write("Player A : {}    Player B : {}".format(score_A,score_B),align="center",font=("Sans Serif",24,"normal"))
    # collision with paddles
    if ball.xcor() > 360 and ball.ycor()<right_paddle.ycor()+50 and ball.ycor()>right_paddle.ycor()-50 :    
        ball.setx(360)
        ball.dx *= -1
    if ball.xcor() < -360 and ball.ycor()<left_paddle.ycor()+50 and ball.ycor()>left_paddle.ycor()-50 :    
        ball.setx(-360)
        ball.dx *= -1
    if score_A ==5 or score_B ==5:
        if score_A > score_B:
            pen.goto(0,0)
            pen.write("Player A Win",align="center",font=("Sans Serif",35,"normal"))
        elif score_A < score_B:
            pen.goto(0,0)
            pen.write("Player B Win",align="center",font=("Sans Serif",35,"normal"))
            