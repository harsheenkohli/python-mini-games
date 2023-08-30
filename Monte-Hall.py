# Choose one of the three doors, an empty one is revealed and 
# participant is allowed to switch from the remaining two choices

import random

doors = [0] * 3
broccoliDoor = [0] * 2
swap = 0 
swapPlays = 0      # no of swap wins
dontSwap = 0 
dontPlays = 0  # no of don't swap wins
x = random.randint(0, 2)   # door having the chocolate
doors[x] = "Chocolate"

while (True) :

    for i in range (3) :
        if (i == x) :
            continue
        doors[i] = "Broccoli"
        broccoliDoor.append(i)

    choice = int(input("Enter your choice from 0 to 2 :\n"))
    if (choice > 2 or choice < 0) :
        print ("Your choice has been cyclically processed as :", (choice % 3))
    choice = choice % 3

    doorOpen = random.choice(broccoliDoor)
    while (choice == doorOpen) :
        doorOpen = random.choice(broccoliDoor)

    ch = input("Do you want to swap? (y / n)\n")
    ch = ch.lower()
    if (ch == "y") :
        swapPlays = swapPlays + 1
        if (doors[choice] == "Broccoli") :
        # initially chose wrong and now swapping
            print("Player wins! You get a chocolate.")
            swap = swap + 1
        else :
            print("Player loses. Eat a broccoli.")
    else :
        dontPlays = dontPlays + 1
        if (doors[choice] == "Broccoli") :
            print("Player loses. Eat a broccoli.")
        else :
            print("Player wins! You get a chocolate.")
            dontSwap = dontSwap + 1

    choice = input("Do you want to play another round? (y / n)\n")
    choice = choice.lower()
    if (choice == "y") :
        continue
    else :
        break

print ("Swap wins :", swap, "/", swapPlays)
print ("Don't swap wins :", dontSwap, "/", dontPlays)
