# Section 1
# importing required modules and declaring default values
import random
import turtle
import time

high_score = 0
delay = 0.1
score = 0


#Section 2
# Creating the board for snake game
board = turtle.Screen()
board.title("SNAKE GAME")
board.bgcolor("aqua")
# the width and height can be put as user's choice
board.setup(width=600, height=600)
board.tracer(0)

# creating the head of the snake
s_head = turtle.Turtle()
s_head.shape("square")
s_head.color("white")
s_head.penup()
s_head.goto(0, 0)
s_head.direction = "Stop"

# creating the food in the game
food = turtle.Turtle()
colors = random.choice(['royalblue', 'gold', 'tomato'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("cornflowerblue")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center",
          font=("candara", 24, "bold"))


#section 3
# giving directions to the snake
#'t' to go up
#'f' to go left
#'g' to go right
#'v' to go down
def go_up():
    if s_head.direction != "down":
        s_head.direction = "up"

def go_left():
    if s_head.direction != "right":
        s_head.direction = "left"

def go_right():
    if s_head.direction != "left":
        s_head.direction = "right"

def go_down():
    if s_head.direction != "up":
        s_head.direction = "down"

def move():
    if s_head.direction == "left":
        x = s_head.xcor()
        s_head.setx(x - 20)
    if s_head.direction == "right":
        x = s_head.xcor()
        s_head.setx(x + 20)
    if s_head.direction == "up":
        y = s_head.ycor()
        s_head.sety(y + 20)
    if s_head.direction == "down":
        y = s_head.ycor()
        s_head.sety(y - 20)



board.listen()
board.onkeypress(go_up, "t")
board.onkeypress(go_down, "v")
board.onkeypress(go_left, "f")
board.onkeypress(go_right, "g")

#Section 4
#Creation of the main game
body = []
while True:
    board.update()
    #to check if the snake collides with the wall
    if s_head.xcor() > 290 or s_head.xcor() < -290 or s_head.ycor() > 290 or s_head.ycor() < -290:
        time.sleep(1)
        s_head.goto(0, 0)
        s_head.direction = "Stop"
        colors = random.choice(['darkorange', 'limegreen', 'slateblue'])
        shapes = random.choice(['square', 'circle'])
        for j in body:
            j.goto(1000, 1000)
        body.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if s_head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # increasing the body size of the snake
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("orange")
        new_body.penup()
        body.append(new_body)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking if the snake collides with itself
    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)
    if len(body) > 0:
        x = s_head.xcor()
        y = s_head.ycor()
        body[0].goto(x, y)
    move()
    for k in body:
        if k.distance(s_head) < 20:
            time.sleep(1)
            s_head.goto(0, 0)
            s_head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for k in body:
                k.goto(1000, 1000)
            k.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)

wn.mainloop()
