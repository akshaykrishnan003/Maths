import sys


order = 2
R = order
C = order 

limit = order * order

number = 0

matrix = [] 
 
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
 

    cStat = False  

    for i in range(R):
        temp = columnSummer(i)
        if ( i+1 < R):
            if (temp == columnSummer(i+1)):
                cStat = True
            else:
                cStat = False
                break

        

    dstat = False
    if (mainDiagonal() == antiDiagonal()):
        dstat = True
    else:
        dstat = False

    if (dstat == cStat == rStat == True):
        printer()
        print ("*******************************")
        sys.exit()

nR = int(input("Enter the limit of max number in the Matrix:"))
for i in range(1,nR):
    for j in range(1,nR):
        for k in range(1,nR):
            for l in range(1,nR):
                if (l != k != j != i):
                    matrix = [[ l*l, k*k ],[ j*j, i*i ]]
                    checker()
                    print ("[",l*l,"\t",k*k,"\t",j*j,"\t",i*i,"]")
                
                
