import turtle
import random

screen = turtle.Screen()
screen.bgcolor("grey")
screen.title("Catch The Turtle")

FONT = ("Arial", 30, "normal")
gridSize = 10
score= 0
gameOver = False

turtleList = []

scoreTurtle = turtle.Turtle()
countDownTurtle = turtle.Turtle()

topHeight = screen.window_height() / 2

xCoordinants = [-20,-10,0,10,20]
yCoordinants = [20,10,0,-10]


def setupScoreTurtle():
    scoreTurtle.hideturtle()
    scoreTurtle.color("#12486B")
    scoreTurtle.penup()
    y = topHeight * 0.9
    scoreTurtle.setposition(0,y)
    scoreTurtle.write("SCORE: 0",move = False, align= "center", font=(FONT))

def makeTurtle(x, y):
    t = turtle.Turtle()

    def handleClick(x,y):
        global score
        score += 1
        scoreTurtle.clear()
        scoreTurtle.write(f"SCORE: {score}",move = False, align= "center", font=(FONT))
        #print(x,y)

    t.onclick(handleClick)
    t.penup()
    t.shape("turtle")
    t.shapesize(1.5,1.5)
    t.goto(x * gridSize, y * gridSize)
    turtleList.append(t)

def setUpTurtles():
    for x in xCoordinants:
        for y in  yCoordinants:
            makeTurtle(x,y)

def hideTurtles():
    for t in turtleList:
        t.hideturtle()

def showTurtlesRandomly():
    if not gameOver:
        hideTurtles()
        random.choice(turtleList).showturtle()
        screen.ontimer(showTurtlesRandomly,500)

def countDown(time):
    global gameOver
    countDownTurtle.hideturtle()
    countDownTurtle.color("#12486B")
    countDownTurtle.penup()
    y = topHeight * 0.9
    countDownTurtle.setposition(0,y -30)
    countDownTurtle.clear()

    if time > 0 :
        countDownTurtle.clear()
        countDownTurtle.write(f"TIME: {time}",move = False, align= "center", font=(FONT))
        screen.ontimer(lambda: countDown(time - 1), 1000)
        hideTurtles()

    else:
        gameOver = True
        countDownTurtle.clear()
        hideTurtles()
        countDownTurtle.write("Game Over!",move = False, align= "center", font=(FONT))
        hideTurtles()

def startGameUp():
    turtle.tracer(0)
    setUpTurtles()
    setupScoreTurtle()
    hideTurtles()
    showTurtlesRandomly()
    countDown(10)
    turtle.tracer(1)


startGameUp()
turtle.mainloop()
