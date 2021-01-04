# A basic code for matrix input from user 
""" order = int(input("Enter the number of rows:"))  """
import sys

order = 2
R = order
C = order 

limit = order * order

number = 0
# Initialize matrix 
matrix = [] 

def numGen():
    global number
    #number = number + 1
    number = 2
    return (number)




# For user input 
""" for i in range(R):		 # A for loop for row entries 
	a =[] 
	for j in range(C):	 # A for loop for column entries 
		a.append(int(numGen())) 
	matrix.append(a)  """



 
def rowSummer(row):
    rSumm = 0
    for i in matrix[row]:
        rSumm = rSumm + i
    return rSumm 

def columnSummer(column):
    cSumm = 0
    for i in range(R):
        cSumm = cSumm + (matrix[i][column])
    return cSumm

def mainDiagonal():
    mSumm = 0
    for i in range(R):
        mSumm = mSumm + (matrix[i][i])
    return mSumm

def antiDiagonal():
    aSumm = 0
    c = R - 1
    for i in range(R):
        aSumm = aSumm + (matrix[i][c])
        c = c - 1
    return aSumm




# For printing the matrix 
def printer():
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], "\t" , end = " ")
        print ()

def checker():
    rStat = False  

    for i in range(R):
        temp = rowSummer(i)
        if ( i+1 < R):
            if (temp == rowSummer(i+1)):
                rStat = True
            else:
                rStat = False
                break
    #if (rStat):
    #    print ("All row equal")
    #else:
    #    print ("Rows not equal")
 

    cStat = False  

    for i in range(R):
        temp = columnSummer(i)
        if ( i+1 < R):
            if (temp == columnSummer(i+1)):
                cStat = True
            else:
                cStat = False
                break
    #if (cStat):
    #    print ("All column equal")
    #else:
    #    print ("Columns not equal")
        

    dstat = False
    if (mainDiagonal() == antiDiagonal()):
        #print ("Diagonals are equal")
        dstat = True
    else:
        #print ("Diagonals not equal")
        dstat = False

    if (dstat == cStat == rStat == True):
        printer()
        print ("*******************************")
        sys.exit()
    #else:
    #    print ("*******************************")

nR = int(input("Enter the limit of max number in the Matrix:"))
for i in range(1,nR):
    for j in range(1,nR):
        for k in range(1,nR):
            for l in range(1,nR):
                """ if (l != k != j != i): """
                matrix = [[ l, k ],[ j, i ]]
                    #printer()
                    #print("*************************")
                checker()
                #printer()
                
                



""" def numGen():
    nR = 3
    for i in range(1,nR):
        for j in range(1,nR):
            for k in range(1,nR):
                for l in range(1,nR):
                    matrix = [
                        [ l, k ],
                        [ j, i ]
                        ]
                    checker()

numGen() """