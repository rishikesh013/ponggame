import turtle as t
import time

# Score varibales
player_a_score = 0
player_b_score = 0

win = t.Screen()    
win.title("Ping-Pong Game") 
win.bgcolor('white')   
win.setup(width=800,height=600) 
win.tracer(0)   

# Function to create the paddle
def paddle(x, angle)-> None:
    x.speed(0)
    x.shape('square')
    x.color("black")
    x.shapesize(stretch_wid=5, stretch_len=1)
    x.penup()
    x.goto(angle, 0)

paddle_left = t.Turtle()
paddle_right = t.Turtle()

paddle(paddle_left, -350)
paddle(paddle_right, 350)

# Creating a pong ball for the game

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('black')
ball.penup()
ball.goto(5,5)
ball_dx = 0.2   
ball_dy = 0.2

# Creating a pen for updating the Score

pen = t.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0                    Player B: 0 ",align="center",font=('Verdana',24,"normal"))


# Moving the left Paddle using the keyboard

def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 90
    paddle_left.sety(y)

# Moving the left paddle down

def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 90
    paddle_left.sety(y)

# Moving the right paddle up

def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 90
    paddle_right.sety(y)

# Moving right paddle down

def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 90
    paddle_right.sety(y)

# Keyboard binding

win.listen()
win.onkeypress(paddle_left_up,"w")
win.onkeypress(paddle_left_down,"s")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")




# Main Game Loop

while True:
    win.update() 

    # Moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # setting up the border

    if ball.ycor() > 290:   # Right top paddle Border
        ball.sety(290)
        ball_dy = ball_dy * -1
        
    
    if ball.ycor() < -290:  # Left top paddle Border
        ball.sety(-290)
        ball_dy = ball_dy * -1
        

    if ball.xcor() > 390:   # right width paddle Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Verdana',24,"normal"))



    if(ball.xcor()) < -390: # Left width paddle Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Verdana',24,"normal"))


    # Handling the collisions with paddles.

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1

    # If score greater than 5 the loop will terminate
    if player_a_score >= 5:
        pen.clear()
        pen.write("Player A Won!!!" ,align="center",font=('Verdana',24,"normal"))
        time.sleep(5)
        break
    
    if player_b_score >= 5:
        pen.clear()
        pen.write("Player B won!!", align="center",font=('Verdana',24,"normal"))
        time.sleep(5)
        break
