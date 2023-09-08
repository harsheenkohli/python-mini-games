"""
         left     right
   top = > 1  2  3  4
           5  6  7  8 
           9  10 11 12
bottom = > 13 14 15 16
"""
import numpy
import turtle
import random

# row = col = 4
# arr = numpy.zeros((row, col))
# arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

row = int(input("Enter the number of rows of matrix :\n"))
col = int(input("Enter the number of columns of matrix :\n"))
arr = numpy.zeros((row, col))

turtle.bgcolor("black")
spiral = turtle.Turtle()
dotDistance = 25

spiral.penup()  # no drawing when moving
listColour = ["white", "yellow", "brown", "red", "blue", "green", 
              "orange", "pink", "violet", "grey", "cyan", "magenta", 
              "purple", "gold", "silver", "lime", "turquoise", "maroon", 
              "navy", "olive", "teal"]

spiral.setposition(-300, 300)   # leftmost position of pen
colour = random.randrange(0, len(listColour))
spiral.color(listColour[colour])

top = left = 0
bottom = row - 1
right = col - 1

counter = 1 # 1->top 2->right 3->bottom 4->left

while (top <= bottom and left <= right) :
    if (counter % 4 == 1) :
        for i in range (left, right + 1) :
            # print(arr[top][i], end=" ")
            spiral.dot()
            spiral.forward(dotDistance)
        counter = counter + 1
        top = top + 1
    elif (counter % 4 == 2) :
        for i in range (top, bottom + 1) :
            # print(arr[i][right], end=" ")
            spiral.dot()
            spiral.forward(dotDistance)
        counter = counter + 1
        right = right - 1
    elif (counter % 4 == 3) :
        for i in range (right, left - 1, -1) :
            # print(arr[bottom][i], end=" ")
            spiral.dot()
            spiral.forward(dotDistance)
        counter = counter + 1
        bottom = bottom - 1
    else :
        for i in range (bottom, top - 1, -1) :
            # print(arr[i][left], end=" ")
            spiral.dot()
            spiral.forward(dotDistance)
        counter = counter + 1
        left = left + 1

    spiral.right(90)

    newCol = random.randrange(0, len(listColour))
    while (colour == newCol) :
        newCol = random.randrange(0, len(listColour))
    colour = newCol
    spiral.color(listColour[colour])
