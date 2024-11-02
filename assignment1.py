import turtle as t

def draw_star():
    t.setup(800, 600)
    t.speed(2)
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.pensize(2)
    t.pencolor("red")
    for i in range(5):
        t.forward(200)
        t.right(144)
    t.done()

draw_star()
