import turtle

man = turtle.Turtle();
man.backward(100)
#green
man.color("green")
man.begin_fill()
man.forward(350)
man.left(90)
man.forward(150)
man.left(90)
man.forward(350)
man.left(90)
man.forward(150)
man.left(90)
man.end_fill()
man.forward(350)

#orange
man.color("orange")
man.begin_fill()
man.left(90)
man.forward(100)
man.left(90)
man.forward(60)
man.left(90)
man.forward(100)
man.left(90)
man.forward(60)
man.end_fill()
man.backward(60)

#black
man.color("black")
man.begin_fill()
man.left(90)
man.forward(100)
man.left(90)
man.forward(60)
man.left(90)
man.forward(100)
man.left(90)
man.forward(60)
man.end_fill()
man.backward(60)

#red
man.color("red")
man.begin_fill()
man.left(90)
man.forward(100)
man.left(90)
man.forward(60)
man.left(90)
man.forward(100)
man.left(90)
man.forward(60)
man.end_fill()
man.backward(60)



turtle.done();