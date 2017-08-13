from graphics import *

def main():
    print("This program plots the growth of a 10 year investment")
    principle = eval(input("Please input the principle amount: $"))
    apr = eval(input("Please provide the annual percentage rate: "))
    apr = apr/10
    # getInvest()

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0k').draw(win)
    Text(Point(20, 180), ' 2.5k').draw(win)
    Text(Point(20, 130), ' 5.0k').draw(win)
    Text(Point(20, 80), ' 7.5k').draw(win)
    Text(Point(20, 30), ' 10.0k').draw(win)

    height = principle * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1,11):
        principle = principle * (1 + apr)
        xll = year * 25 + 40
        height = principle * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    input("Press <Enter> to quit")
    win.close()

main()
# def getInvest():
        
