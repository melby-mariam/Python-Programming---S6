import turtle
board=turtle.Turtle()
turtle.bgcolor("blue")
turtle.pencolor("red")
turtle.title("My Turtle")
count=0
while(count<360):
    board.forward(2)
    board.left(1)
    count+=1

turtle.done()


# turtle.circle(60)
# turtle.dot(20)