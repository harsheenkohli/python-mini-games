# Permutations

import random

def playJumbleUp() :
    print("Welcome to ANAGRAM MAGIC!✨\n")
    pl1Name = input("Player 1, please enter your name :\n")
    pl2Name = input("Player 2, please enter your name :\n")
    print("RULES :\nEach player gets 2 guesses per word. \nGuess 1 : 10 points \nGuess 2 : 5 points")

    p1Points = p2Points = 0
    playerTurn = pl1Name
    playerGuess = pl2Name

    while(True) :
        turn(playerTurn)
        print(playerTurn, ": Enter a word :")
        word = input()
        word = word.upper()
        
        jumbled = jumbleWord(word)
        print("Unjumble the sequence,",  playerGuess + "!\n"  + jumbled)     

        if (playerTurn == pl1Name) :
            p2Points += game(word)
            playerTurn = pl2Name
            playerGuess = pl1Name
            continue
        if (playerTurn == pl2Name) :
            p1Points += game(word)
            choice = input("Enter 0 to exit, and any other character to continue : ")
            if (choice == '0') :
                winner(pl1Name, pl2Name, p1Points, p2Points)
                break
            else :
                playerTurn = pl1Name
                playerGuess = pl2Name
                displayPoints(pl1Name, pl2Name, p1Points, p2Points)
           

def turn(playerTurn) :
    print(playerTurn + "'s turn to give a word!")

def jumbleWord(word) :
    jumbled = list(word)
    random.shuffle(jumbled)
    return convert(jumbled)

def convert(jumbled) :
    word = ""
    for char in jumbled :
        word += char
    return word

def game(word) :
    points = 0    
    guess = input("Guess 1 :\n")
    guess = guess.upper()   
    if (guess == word) :
            points = 10
            print("You guessed right!")
    else :
        print("Try again!")
        guess = input("Guess 2 : \n")
        guess = guess.upper()
        if(guess == word) :
            points = 5
            print("You guessed right!")
        else :
            print("Incorrect guesses :(")
    return points

def winner(pl1Name, pl2Name, p1Points, p2Points) :
    print("Points : \n" + pl1Name, ":", p1Points, "\n" + pl2Name, ":", p2Points)
    if (p1Points > p2Points) :
        print(pl1Name, "wins!")
    elif (p1Points < p2Points) :
        print(pl2Name, "wins!")
    else :
        print("Match drawn!")

def displayPoints(pl1Name, pl2Name, p1Points, p2Points) :
    print("Points tally :")
    print(pl1Name, ":", p1Points, "\t", pl2Name, ":", p2Points)
    if (p1Points > p2Points) :
        print(pl1Name, "is currently in lead!")
    elif (p1Points < p2Points) :
        print(pl2Name, "is currently in lead!")
    else :
        print("Scores levelled!")
    print()

playJumbleUp()
