import turtle
t = turtle.Turtle()
t.pensize(40)
def move():
    t.forward(20)
def turn_left():
    t.left(20)
def move2():
    t.back(20)
def turn_right():
    t.right(20)
turtle.listen()
turtle.onkeypress(move2, 'Down')
turtle.onkeypress(move, 'Up')
turtle.onkeypress(turn_left, 'Left')
turtle.onkeypress(turn_right, 'Right')
turtle.done()
