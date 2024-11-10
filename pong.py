import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Daniel Pong")
wn.bgcolor("Black")
wn.setup(width=1000, height=800)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-490, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
#paddle_b.penup()
paddle_b.goto(480, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("red")
#ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

# Score
score_a = 0
score_b = 0

# Pen for displaying score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Player A: 0  Player B: 0", align="center", font=("SF Pro", 24, "normal"))

# Function to move paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 330:
        paddle_a.sety(y + 20)

# Function to move paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -330:
        paddle_a.sety(y - 20)

# Function to move paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 330:
        paddle_b.sety(y + 20)

# Function to move paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -330:
        paddle_b.sety(y - 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    if ball.ycor() > 390:
        ball.sety(390)
        ball.dy *= -1
    
    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1
    
    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("SF Pro", 24, "normal"))
    
    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("SF Pro", 24, "normal"))
    
    # Paddle and ball collisions
    if (ball.dx > 0) and (470 > ball.xcor() > 460) and (paddle_b.ycor() + 60 > ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(460)
        ball.dx *= -1

    if (ball.dx < 0) and (-450 < ball.xcor() < -440) and (paddle_a.ycor() + 60 > ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-440)
        ball.dx *= -1
