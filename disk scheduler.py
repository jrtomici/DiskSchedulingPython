import turtle
from turtle import *
bgcolor("black")
MAX = 199

def main():
    # turtle setup
    turtle.title("Disk Scheduler")
    turtle.setup(500, 500)
    t = turtle.Turtle()
    t.speed(0)
    t.color("white")
    # take user input for cylinder list
    cylinders = []
    a = numinput("Setup", "Number of cylinders: ", minval=2, maxval=10)
    for i in range(int(a)):
        c = numinput("Setup", "Cylinder position " + str(i+1) + ": ", minval=0, maxval=199)
        cylinders.append(c)
    cylindersCopy1 = cylinders.copy()
    cylindersCopy2 = cylinders.copy()
    # draw algorithms
    drawAxis(t, cylinders)
    t.speed(3)
    t.pencolor("magenta")
    drawAlgo(t, fcfs(cylinders))
    t.pencolor("cyan")
    drawAlgo(t, sstf(cylinders))
    t.pencolor("lime")
    drawAlgo(t, scan(cylindersCopy1))
    t.pencolor("yellow")
    drawAlgo(t, cscan(cylindersCopy2))
    turtle.done()

# First Come First Serve
def fcfs(cylinders):
    print("RED: First Come First Serve.\nCylinder order: ", end = '')
    order = []
    movement = 0
    for i, c in enumerate(cylinders):
        print(str(int(c)) + " ", end = '')
        order.append(int(c))
        if i != len(cylinders) - 1:
            movement += abs(c - cylinders[i + 1])
    print("\nTotal head movement: " + str(int(movement)))
    return order

# Shortest Seek Time First (Closest Cylinder Next)
def sstf(cylinders):
    print("\nBLUE: Shortest Seek Time First (Closest Cylinder Next).\nCylinder order: ", end = '')
    order = []
    movement, seekTime, n = 0, 999, 0
    print(str(int(cylinders[0])) + " ", end = '')
    order.append(int(cylinders[0]))
    for i, c in enumerate(cylinders):
        for j, d in enumerate(cylinders):
            if i != j:
                # find the shortest possible seek time and keep track of index
                if abs(c - d) < seekTime:
                    seekTime = abs(c - d)
                    n = j
        if i != len(cylinders) - 1:
            movement += abs(c - cylinders[n])
            print(str(int(cylinders[n])) + " ", end = '')
            order.append(int(cylinders[n]))
        # disregard selected cylinder
        cylinders[i] = seekTime = 999
        # swap selected cylinder with next cylinder in the list
        if i != len(cylinders) - 1:
            temp = cylinders[i + 1]
            cylinders[i + 1] = cylinders[n]
            cylinders[n] = temp
    print("\nTotal head movement: " + str(int(movement)))
    return order

# SCAN (Elevator)
def scan(cylinders):
    print("\nGREEN: SCAN (Elevator).\nCylinder order: ", end = '')
    order = []
    movement = start = 0
    head = cylinders[0]
    cylinders.sort()
    cylinders.reverse()
    movement += cylinders[0]
    # find head starting position
    for i, c in enumerate(cylinders):
        if c == head:
            start = i
            movement += c
    # start moving left
    for i, c in enumerate(cylinders):
        if i != len(cylinders) and i >= start:
            print(str(int(c)) + " ", end = '')
            order.append(int(c))
    order.append(0)
    cylinders.reverse()
    # find head starting position again
    start = len(cylinders) - 1 - start
    # skip back to start and move right
    for i, c in enumerate(cylinders):
        if i != len(cylinders) and i > start:
            print(str(int(c)) + " ", end = '')
            order.append(int(c))
    print("\nTotal head movement: " + str(int(movement)))
    return order

# Circular SCAN (C-SCAN)
def cscan(cylinders):
    print("\nYELLOW: Circular SCAN (C-SCAN).\nCylinder order: ", end = '')
    order = []
    movement = start = 0
    head = cylinders[0]
    cylinders.sort()
    # find head starting position
    for i, c in enumerate(cylinders):
        if c == head:
            start = i
    # start moving right
    for i, c in enumerate(cylinders):
        if i >= start:
            print(str(int(c)) + " ", end = '')
            order.append(int(c))
    # wrap around to start of disk and continue moving right
    order.append(MAX)
    order.append(0)
    for i, c in enumerate(cylinders):
        if i < start:
            print(str(int(c)) + " ", end = '')
            order.append(int(c))
    movement += (MAX - cylinders[start] + MAX)
    if start != 0:
        movement += cylinders[start - 1]
    print("\nTotal head movement: " + str(int(movement)))
    return order

def drawLine (t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.penup()

def labelPoint (t, x, y, label):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(label)
    t.penup()

def drawAxis(t, cylinders):
    # draw the axis
    t.pencolor("white")
    drawLine(t, -200, 150, 200, 150)
    # label the axis
    drawLine(t, -200, 145, -200, 155)
    labelPoint(t, -200, 160, 0)
    drawLine(t, 199, 145, 199, 155)
    labelPoint(t, 199, 160, 199)
    for i in cylinders:
        drawLine(t, 2*(i-100), 145, 2*(i-100), 155)
        labelPoint(t, 2*(i-100), 160, str(int(i)))
    # key
    t.pencolor("magenta")
    labelPoint(t, -200, 180, "FCFS")
    t.pencolor("cyan")
    labelPoint(t, -150, 180, "SSTF")
    t.pencolor("lime")
    labelPoint(t, -100, 180, "SCAN")
    t.pencolor("yellow")
    labelPoint(t, -50, 180, "C-SCAN")

def drawAlgo(t, order):
    currentY = 135
    goDown = 300 / len(order)
    t.penup()
    t.goto(2*(order[0]-100), currentY)
    t.pendown()
    for i in order:
        if i != i+1:
            t.goto(2*(i-100), currentY)
            currentY -= goDown
    t.penup()

main()
