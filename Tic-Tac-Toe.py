# min max strategy => minimise opponent's chances of winning and maximise yours
# 3x3 board => 2D array

import numpy

board = numpy.array([['_'] * 3, ['_'] * 3, ['_'] * 3])

pl1Symb = 'X'
pl2Symb = 'O'
pl1Name = input("Player 1, enter your name for symbol X :\n")
pl2Name = input("Player 2, enter your name for symbol O :\n")

def checkRows (symbol):
    for row in range (3) :
        count = 0
        for col in range (3) :
            if (board[row][col] == symbol) :
                count = count + 1
            else :
                break
        if (count == 3) :
            return True
    return False

def checkCols (symbol):
    for col in range (3) :
        count = 0
        for row in range (3) :
            if (board[row][col] == symbol) :
                count = count + 1
            else :
                break
        if (count == 3) :
            return True
    return False

def checkDiag (symbol) :
    leftDiag = 0
    rightDiag = 0
    for idx in range(3) :
        if (board[idx][idx] == symbol) :
            leftDiag = leftDiag + 1
        if (board[idx][2 - idx] == 0) :
            rightDiag = rightDiag + 1
    if(leftDiag == 3 or rightDiag == 3) :
        return True
    return False

def won(symbol) :
    return checkRows(symbol) or checkCols(symbol) or checkDiag(symbol)

def place(symbol) :
    print(numpy.matrix(board))
    while (True) :
        print("Enter your row and column number respectively (1 to 3):")
        row = int(input()) - 1
        col = int(input()) - 1
        if (row > 2 or col > 2 or row < 0 or col < 0 or board[row][col] != '-') :
            print("Please try again")
        else :
            board[row][col] = symbol
            break

def play() :
    for turn in range (10) :
        if (turn == 9) :
            print("Match drawn!")
            break
        if (turn % 2 == 0) :
            print(pl1Name + "'s turn.")
            place(pl1Symb)
            if (won(pl1Symb)) :
                print(pl1Name, "won!")
                break
        else :
            print(pl2Name + "'s turn.")
            place(pl2Symb)
            if (won(pl2Symb)) :
                print(pl2Name, "won!")
                break
    print(board)

play()
