from PIL import Image
# PIL package, Image library
import random

end = 100   # reaching 100 means won the game

def displayResult(winnerName, winnerToken, loserName, loserToken, endStatus) :
    print(winnerName, "wins!")
    if (endStatus == 0) :
        print(loserName, "loses on account of quitting.")
    print("Final token positions :")
    print(winnerName, ":", winnerToken)
    print(loserName, ":", loserToken)

def checkLadder(token) :
    ladder = {8 : 26, 21 : 82, 43 : 77, 50 : 91, 54 : 93, 
              62 : 96, 66 : 87, 80 : 100}
    if token in ladder.keys() :
        print("Your current token position :", token)
        print("You encountered a ladder!")
        print("Moving up to", ladder[token])
        return ladder[token]
    return token
    
def checkSnake(token) :
    snake = {44 : 22, 46 : 5, 48 : 9, 52 : 11, 55 : 7, 59 : 17, 
             64 : 36, 69 : 33, 73 : 1, 83 : 19, 92 : 51, 95 : 24, 98 : 28}
    if token in snake.keys() :
        print("Your current token position :", token)
        print("You encountered a snake!")
        print("Trailing down to", (snake[token]))
        return snake[token]
    return token

def show_board() :
    img = Image.open('d:\TJCP\Week 7\Snl-Board.jpg')
    img.show()

def play() :
    pl1Name = input("Player 1, Please enter your name :\n")
    pl2Name = input("Player 2, Please enter your name :\n")
    pl1Token = pl2Token = 0   # initial placement of tokens

    turn = 1
    while(True) :
        if (turn % 2 != 0) :
            print(pl1Name + "'s turn :")
            choice = input("Do you want to continue? (Y/N)")
            choice = choice.upper()

            if (choice == "N") :
                displayResult(pl1Name, pl1Token, pl2Name, pl2Token, 0)
                break

            dice = random.randint(1, 6)
            print("The dice rolled", dice)

            if ((pl1Token + dice) > end) :
                print("Cannot cross 100, better luck next turn!")
                turn = turn + 1
                continue

            pl1Token = pl1Token + dice

            pl1Token = checkLadder(pl1Token)
            pl1Token = checkSnake(pl1Token)
            if (pl1Token == end) :
                displayResult(pl1Name, pl1Token, pl2Name, pl2Token, 1)
                break

            print("Your current token position :", pl1Token)
            turn = turn + 1
        
        else :
            print(pl2Name + "'s turn :")
            choice = input("Do you want to continue? (Y/N)")
            choice = choice.upper()

            if (choice == "N") :
                displayResult(pl2Name, pl2Token, pl1Name, pl1Token, 0)
                break

            dice = random.randint(1, 6)
            print("The dice rolled", dice)

            if ((pl2Token + dice) > end) :
                print("Cannot cross 100, better luck next turn!")
                turn = turn + 1
                continue

            pl2Token = pl2Token + dice
            
            pl2Token = checkLadder(pl2Token)
            pl2Token = checkSnake(pl2Token)
            if (pl2Token == end) :
                displayResult(pl2Name, pl2Token, pl1Name, pl1Token, 1)
                break

            print("Your token position :", pl2Token)

            turn = turn + 1

show_board()
play()
