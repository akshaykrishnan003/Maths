import sys


order = 3
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
    f = open("fsum_3.txt", "a")
    for i in range(R):
        for j in range(C):
            print(matrix[i][j], "\t" , end = " ")
            f.write(str(matrix[i][j]))
        print ()
    f.write("\n")
    f.close()


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

nR = int(input("Enter the limit of max number in the Matrix:"))
for i in range(1,nR):
    for j in range(1,nR):
        for k in range(1,nR):
            for l in range(1,nR):
                for m in range(1,nR):
                    for n in range(1,nR):
                        for o in range(1,nR):
                            for p in range(1,nR):
                                for q in range(1,nR):
                                    if (i != j != k != l != m != n != o != p != q):
                                        matrix = [[ q, p, o],[ n, m, l],[ k, j, i ]]
                                        checker()
                                    print ("[",i,"\t",j,"\t",k,"\t",l,"\t",m,"\t",n,"\t",o,"\t",p,"\t",q,"]")
                
                
