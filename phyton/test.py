import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.setup(width = 400, height= 600)
wn.title("hello")
wn.bgcolor("orange")
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, -50)
text.color("black")
text.write("button", align="center", font=("Arial", 20, 'bold'))
t.penup()
t.goto(0, -50)
t.shape("square")
t.shapesize(stretch_wid=2, stretch_len=6)
t.color("blue")
def clicked(a, b):
    text.write("clicked", align="center")
t.onclick(clicked)

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
