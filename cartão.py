import turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
e = t.getscreen()
t.begin_fill()
for i in range(4):
    t.color('green','green')
    t.forward(100)
    t.right(90)
t.end_fill()
t.forward(100)
t.begin_fill()
for i in range(4):
    t.color('red','red')
    t.forward(100)
    t.right(90)
t.end_fill()
t.penup()
t.right(90)
t.forward(100)
t.left(180)
t.forward(50)
t.right(180+90)
t.forward(50)
t.right(180)
t.forward(25)
t.right(90)
t.pendown()
t.begin_fill()
for c in range(1):
    t.color('yellow', 'yellow')
    t.circle(30)
    t.penup()
    t.pendown()
    t.end_fill()
e.mainloop()