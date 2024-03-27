import turtle

turtle_interactive = turtle.Screen()
turtle_interactive.bgcolor("red")
turtle_interactive.title("interactive process")
turtle_instance = turtle.Turtle()
def turtle_forward():
    turtle_instance.forward(100)
def turtle_left():
    turtle_instance.left(90)
def turtle_right():
    turtle_instance.right(90)
def clear_screen():
    turtle_instance.clear()
def return_home():
    turtle_instance.home()
def turtle_penup():
    turtle_instance.penup()
def turtle_pendown():
    turtle_instance.pendown()

turtle_interactive.listen()
turtle_interactive.onkey(fun=turtle_forward, key="space")
turtle_interactive.onkey(fun=turtle_left, key="Down")
turtle_interactive.onkey(fun=turtle_right, key="Up")
turtle_interactive.onkey(fun=clear_screen, key="c")
turtle_interactive.onkey(fun=return_home, key="d")
turtle_interactive.onkey(fun=turtle_penup, key="p")
turtle_interactive.onkey(fun=turtle_pendown, key="o")
turtle.mainloop()
