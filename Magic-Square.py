# sum = n * (n^2 + 1) / 2
# position of 1 : always mid row last column => (n/2, n - 1)
# if 1 at (p, q) => 2 at (p - 1, q + 1)
# Cond - 1: if p == -1 => p = n - 1
# Cond - 2: if q == n => q = 0
# Cond - 3: if calc pos has a number => p++ & q = q - 2
# Cond - 4: if p == -1 and q == n => p = 0 & q = n - 2


def magic_square(n) :

    magicSquare = [[0 for i in range(n)] for j in range(n)]     
    # put 0 for i from 0 to 2 in this list

    # position of 1
    i = n // 2   # row number
    j = n - 1   # column number
    num = n * n
    count = 1       # for element

    while(count <= num) :
        if(i == -1 and j == n) :
            # cond - 4
            i = 0
            j = n - 2
        else :
            if (j == n) :
                # cond - 2
                j = 0
            if(i < 0) :
                # cond - 1
                i = n - 1

        if (magicSquare[i][j] != 0) :
            # cond - 3
            i = i + 1
            j = j - 2
            continue 
        # skip rest of the statements and recheck till a 0 is found
        magicSquare[i][j] = count
        count = count + 1
        i = i - 1
        j = j + 1

    for i in range(n) :
        for j in range(n) :
            print(f'{magicSquare[i][j]:2d}', end = " ")
        print()

n = input("Enter the number of rows/columns of the magic square : ")
if (int(n) % 2 == 0) :
    print("Magic Square for even number of rows/columns is not possible.")
else :
    magic_square(int(n))
