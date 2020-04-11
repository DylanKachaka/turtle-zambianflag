import turtle

star = turtle.Turtle();

star.color("red", "yellow")
star.begin_fill()
for move in range(69):
    star.forward(200)
    star.left(165)
star.end_fill()



turtle.done();