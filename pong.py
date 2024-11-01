# Pong Game for Fun
# Developed by Salahebrahimipour
#This game is just for fun! Fork it or maybe play it! :)


import turtle
import os 


wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("#1E202F")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score track

score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("Yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2


# Score line
pen = turtle.Turtle()
pen.speed(0)
pen.color("Yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, -280)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 14, "bold"))



# Moving Paddles 
def paddle_a_upwards():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_downwards():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_upwards():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_downwards():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)




#Listen For Keyboard Input

wn.listen()
wn.onkeypress(paddle_a_upwards, "w")
wn.onkeypress(paddle_a_downwards, "s")
wn.onkeypress(paddle_b_upwards, "Up")
wn.onkeypress(paddle_b_downwards, "Down")




# Game Playground Area

while True:
    wn.update()

    #Let the ball bounce
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #hitting the border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.mp3&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.mp3&")


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}". format(score_a, score_b), align="center", font=("Courier", 14, "bold"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}". format(score_a, score_b), align="center", font=("Courier", 14, "bold"))

    
    # Collusion process 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.mp3&")


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.mp3&")
