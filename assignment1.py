def draw_python():
    import turtle as t
    t.setup(800, 300, 200, 200)
    t.penup()
    t.fd(-200)
    t.pendown()
    t.seth(-50)
    t.pensize(25)
    t.pencolor("blue")
    for i in range(4):
        t.circle(5, 100)
        t.circle(-100, 50)
    t.circle(50, 100 / 2)
    t.fd(50)
    t.circle(20, 200)
    t.fd(50 * 2 / 3)
    t.done()


print("----- Welcome to the drawing system ----")
draw_python()
