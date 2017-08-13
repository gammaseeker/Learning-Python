import graphics
from graphics import *

# win = graphics.GraphWin()
# win.close()

p = Point(50, 60)
print(p.getX())
print(p.getY())
win = GraphWin()
p.draw(win)
p2 = Point(140, 100)
p2.draw(win)

win = GraphWin('Shapes')
center = Point(100, 100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)
label = Text(center, "Red Circle")
label.draw(win)
rect = Rectangle(Point(30, 30), Point(70, 70))
rect.draw(win)
line = Line(Point(20, 30), Point(180, 165))
line.draw(win)
oval = Oval(Point(20, 150), Point(180, 199))
oval.draw(win)

win.mainloop()