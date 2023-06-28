import math
import matplotlib.pyplot as plt
from array import *
import numpy as np
import random
import itertools
answer = np.array([[0,4,4,4,0],[5,5,0,5,0],[3,0,0,5,4],[1,2,3,0,0],[2,0,3,5,0]])
xGCD = [0,1,1,5,4]
yGCD = [0,5,3,123,1]


def concatinator(array):
    temp = ""
    output = []
    for i in range(len(array)):
        if(array[i]!=0):
            temp+=str(array[i])
        else:
            if(len(temp)>0):
                output.append(int(temp))
            temp = ""
    if(len(temp)>0):
        output.append(int(temp))
    return output

def areRowsValid(xGCD,yGCD,array):
    output = [[],[]]
    for i in range(len(array)):
        x = concatinator(array[i])
        if(len(x)==0):
            return False
        if(len(x)>0 and yGCD[i]!=0):
            if(math.gcd(*x) != yGCD[i]):
                output[0].append(i)
                # print("Row {"+str(i)+"} is invalid")
        else:
            if(math.gcd(x[0],x[0])!=x[0]):
                output[0].append(i)
                # print("Row {"+str(i)+"} is invalid")

    array = np.transpose(array)
    for j in range(len(array)):
        x = concatinator(array[j])
        if(len(x)==0):
            return False
        if(len(x)>1 and xGCD[j]!=0):
            if(math.gcd(*x) != xGCD[j]):
                output[1].append(j)
                # print("Col {"+str(j)+"} is invalid")
            else:
                if(math.gcd(x[0],x[0])!=x[0]):
                    output[0].append(j)
                    # print("Col {"+str(i)+"} is invalid")
    if(len(output[0])<1 and len(output[1])< 1):
        return True
    else:
        return False

def generateRandomGrid(size):
    empty = np.empty((size,size), dtype= int)
    for i in range(size):
        for j in range(size):
            x= random.randrange(0,size+1,1)
            empty[i][j] = x
    return empty

def solve(size,xGCD,yGCD):
    solved = False
    while solved != True:
        answer = generateRandomGrid(size)
        solved = areRowsValid(xGCD,yGCD,answer)
    print(answer)

def isRowValid(row,GCD,traversedRows):
    for x in traversedRows:
        if(list(x)==list(row)):
            return False
    if(sum(row)==0):
        return False
    x = concatinator(row)
    if(math.gcd(*x)==GCD):
        return True
    if(GCD == 0):
        return True
    if(len(x)==1):
        if(x[0]==GCD):
            return True
    return False

def solve2(size,xGCD,yGCD):
    empty = np.zeros((size,size), dtype= int)
    temp =0
    number = []
    for i in range(size):
        print("valid rows for row "+str(i))
        number.append(0)
        for j in range(size):
            number.append(j+1)
            for x in itertools.product(number, repeat=size):
                if(isRowValid(x,yGCD[i])):
                    empty[i]=x
                    temp = j
    tranposed = np.transpose(empty)
    # for i in range(len(tranposed)):
    #     if(isRowValid(tranposed[x],xGCD[x])==False):
    #         print("failed")
    print(empty)

def isValid(array,xGCD,yGCD):
    for i in range(len(array)):
        if(isRowValid(array[i],yGCD[i])==False):
            return False
    tranposed = np.transpose(array)
    for i in range(len(tranposed)):
        if(isRowValid(tranposed[i],xGCD[i])==False):
            return False
    return True


def solve3(size,xGCD,yGCD,empty,count):

    if(isValid(empty,xGCD,yGCD)):
        print("Following is Valid: ")
        print(empty)
        return empty
    number = [0,1,2,3,4,5]
    for i in range(size):
        pos = np.array(list(itertools.product(number, repeat=size)))
        for x in range(len(pos)):
            if(isRowValid(pos[x],yGCD[i])):
                empty[i]=x
                print(empty)
                break

def generateListOfNextValidRows(xGCD,yGCD,currentGrid):
    for i in range(len(currentGrid)):
        for x in itertools.product([0,i+1], repeat=len(currentGrid)):
            if(isRowValid(x,yGCD[0])):
                    currentGrid[0] = x
                    lastDigit = currentGrid[0][-1]
                    currentGrid = np.transpose(currentGrid)
                    for x in itertools.product([0,i+1], repeat=len(currentGrid)-1):
                        if(isRowValid(list(x),xGCD[4])):
                            currentGrid[4] = x
                            currentGrid = np.transpose(currentGrid)
                            return currentGrid
def checkTranspose(array,xGCD):
    array = np.transpose(array)
    for x in range(len(array)):
        if(isRowValid(array[x],xGCD[x],[])==False):
            return False
    return True


def GenSolve(xGCD,yGCD,currentValidGrid,traversedRows,x,y):
    listOfValids = [[],[],[],[],[]]

    for j in range(len(currentValidGrid)):
            for x in itertools.product([0,1,2,3,4,5], repeat=len(currentValidGrid)):
                    if(isRowValid(x,yGCD[j],traversedRows)):
                        if(len(np.unique(list(x)))<=j+2):
                            listOfValids[j].append(x)

    # test = np.array([listOfValids[0][0],listOfValids[1][0],listOfValids[2][0],listOfValids[3][0],listOfValids[4][0]])
    print(len(listOfValids[0]))
    print(len(listOfValids[1]))
    print(len(listOfValids[2]))
    print(len(listOfValids[3]))
    print(len(listOfValids[4]))
    # print(listOfValids[2])
    possibleAnswers = []
    for one in listOfValids[0]:
        for two in listOfValids[1]:
            for three in listOfValids[2]:
                for four in listOfValids[3]:
                    # for five in listOfValids[4]:
                        test = np.array([one,two,three,four,[2,0,3,5,0]])
                        if(checkTranspose(test,xGCD)):
                            possibleAnswers.append(test)
    print("done")
    print(len(possibleAnswers))
    for x in possibleAnswers:
        if(np.array_equal(x, answer)):
            print(x)
            print("found it")

def GenSolve2(xGCD,yGCD,empty,rowsFilled=0,sizeRemaning=5,traversedRows=[[],[],[],[],[]],traversedCols=[[],[],[],[],[]],count=0,continueBackTrack=False):
    print("start: \n ", empty)
    # print("rows: \n",rowsFilled)
    # print(traversedRows)
    # print(traversedCols)
    if(rowsFilled==5):
        print("valid")
        print(empty)
    rowValid = False
    colValid = True
# fill row
    if(continueBackTrack != True):
        for x in itertools.product([0,1,2,3,4,5], repeat=sizeRemaning):
                    temp = sizeRemaning
                    while temp < len(empty):
                        x = x+((empty[rowsFilled][temp]),)
                        temp+=1
                    if(isRowValid(x,yGCD[rowsFilled],traversedRows[rowsFilled])):
                        rowValid = True
                        empty[rowsFilled] = x 
                        break
        traversedRows[rowsFilled].append(empty[rowsFilled])
        if(rowValid): 
        # fill col
            empty = np.transpose(empty)
            index = len(empty)-rowsFilled-1
            for x in itertools.product([0,1,2,3,4,5], repeat=sizeRemaning):
                    temp = 0
                    x =list(x)
                    while temp < rowsFilled:
                        x.insert(temp,empty[index][temp])
                        temp+=1
                    if(isRowValid(x,xGCD[index],traversedCols[index])):
                        empty[index] = x
                        colValid = True
                        break
            traversedCols[index].append(empty[index])
            empty = np.transpose(empty)
            sizeRemaning-=1
            rowsFilled+=1
            print("filled row and col")
            return GenSolve2(xGCD,yGCD,empty,rowsFilled,sizeRemaning,traversedRows,traversedCols,count)
    
        # if(False):
        #     x = []
        # for i in range(sizeRemaning):
        #     x.append(0)
        # temp = sizeRemaning
        # while temp < len(empty):
        #         x.append(empty[rowsFilled][temp])
        #         temp+=1
        # empty[rowsFilled]= x
        # print("try row again")
        # return GenSolve2(xGCD,yGCD,empty,rowsFilled,sizeRemaning,traversedRows,traversedCols,count)
    
    if(count<2):

        # # reset col
        empty = np.transpose(empty)

        x = [0 for x in range(len(empty))]

        temp = 0
        index = len(empty)-rowsFilled
        while temp < rowsFilled:
                x[temp]=(empty[rowsFilled][temp])
                temp+=1
        empty[index]= x
        empty = np.transpose(empty)

        # reset rows
        x = [0 for x in range(len(empty))]
        temp = rowsFilled
        while temp < (len(empty)):
                x[temp] = empty[rowsFilled-1][temp]
                temp+=1
        empty[rowsFilled-1]= x

        sizeRemaning+=1
        rowsFilled-=1
        print("backtrack",np.transpose(empty))
        count+=1
        return GenSolve2(xGCD,yGCD,empty,rowsFilled,sizeRemaning,traversedRows,traversedCols,count,True)




empty = np.zeros((5,5), dtype= int)
empty[0]=[0,4,4,4,0]
empty[1]=[0,0,0,0,0]
empty[2]=[0,0,0,0,4]
empty[3]=[0,0,0,0,0]
empty[4]=[0,0,0,0,0]
xG9 = [5,1,6,1,8,1,22,7,8]
xG9 = [55,1,6,1,24,3,6,7,2]
traversedRows = []

# GenSolve2(xGCD,yGCD,empty,1,4)

# empty = np.zeros((5,5), dtype= int)
# empty[0]=[0,0,0,0,1]
GenSolve2(xGCD,yGCD,empty,1,4)
# print(isRowValid(empty[0],xGCD[0],[(0, 0, 0, 0, 1),(1, 1, 2, 0, 4)]))
# GenSolve2(xG9,xG9,empty,0,9)
# empty = np.zeros((5,5), dtype= int)
# empty[0]=[0,4,4,4,0]
# empty[1]=[5,5,0,5,0]
# empty[2]=[0,0,0,5,4]
# empty[3]=[0,0,0,0,0]
# empty[4]=[0,0,0,5,0]
# GenSolve2(xGCD,yGCD,empty,2,3)
# empty = np.zeros((5,5), dtype= int)
# empty[0]=[0,4,4,4,0]
# empty[1]=[5,5,0,5,0]
# empty[2]=[3,3,3,5,4]
# empty[3]=[0,0,3,0,0]
# empty[4]=[0,0,0,5,0]
# GenSolve2(xGCD,yGCD,empty,3,2)
    # empty = np.transpose(empty)
    # print(empty)
    # for i in range(len(empty)):
    #     for x in itertools.product([0,i+1], repeat=sizeRemaning-1):
    #                 x = x+(empty[2][3],empty[2][4])
    #                 if(isRowValid(x,yGCD[2],traversedRows)):
    #                     empty[2] = x
    #                     listOfValids.append(x)
                       
    # empty = np.transpose(empty)
    # for x in itertools.product([0,3], repeat=sizeRemaning-1-1):
                   
    #                 x = (empty[2][0],empty[2][1],empty[2][2])+x
    #                 if(isRowValid(x,xGCD[2],traversedRows)):
    #                     empty[2] = x

    # empty = np.transpose(empty)
    # for i in range(len(empty)):
    #     for x in itertools.product([0,1,2], repeat=2):
    #                 x = x+(empty[3][2],empty[3][3],empty[3][4])
    #                 print(x)
    #                 if(isRowValid(x,yGCD[3],traversedRows)):
    #                     empty[3] = x
    #                     listOfValids.append(x)
                       
    # empty = np.transpose(empty)
    # for x in itertools.product([0,1,2], repeat=sizeRemaning-1-1-1):
    #                 x = (empty[1][0],empty[1][1],empty[1][2],empty[1][3])+x
    #                 if(isRowValid(x,xGCD[1],traversedRows)):
    #                     empty[1] = x
    # empty = np.transpose(empty)
   

                        
                        # test = np.transpose(test)
                        # count = 0
                        # for i in range(len(currentValidGrid)):
                        #     if(isRowValid(x,xGCD[i],traversedRows)):
                        #         count = count+1
                        # if(count==5):
                        #     print(np.transpose(test))
    

                        # return GenSolve(xGCD,yGCD,currentValidGrid,traversedRows,count,Rows)
    # else:
    #     i = 4
    #     nums = [0,i+1]
    #     for x in itertools.product(nums, repeat=len(currentValidGrid)):
    #                 if(isRowValid(x,xGCD[len(currentValidGrid)-1],traversedRows)):
    #                     currentValidGrid[len(currentValidGrid)-1]=x
    #                     traversedRows.append(x)
    #                     print(currentValidGrid)
    #                     currentValidGrid = np.transpose(currentValidGrid)
    #                     Rows =True
    #                     return GenSolve(xGCD,yGCD,currentValidGrid,traversedRows,count,Rows)
                    
                # for y in itertools.product([0,i+1], repeat=len(currentValidGrid)):
                #         print(y)
                #         if(isRowValid(y,xGCD[4-count],traversedRows)):
                #             currentValidGrid[4-count] = y
                #             currentValidGrid = np.transpose(currentValidGrid)
                #             return GenSolve(xGCD,yGCD,currentValidGrid,traversedRows,count)
                        
    # currentValidGrid = np.zeros((5,5), dtype= int)
    # count = count-1
    # return GenSolve(xGCD,yGCD,currentValidGrid,traversedRows,count)

    # print("No Path Found")
    # return False

# empty = np.zeros((9,9), dtype= int)
# generateListOfNextValidRows([5,1,6,1,8,1,22,7,8], [55,1,6,1,24,3,6,7,2],empty)


# print(generateListOfNextValidRows(xGCD, yGCD,empty))

# solve3(9, [5,1,6,1,8,1,22,7,8], [55,1,6,1,24,3,6,7,2],empty,0)
# solve2(5, xGCD, yGCD)
# solve2(9, [5,1,6,1,8,1,22,7,8], [55,1,6,1,24,3,6,7,2])
# solve(5,xGCD,yGCD)
# print(generateRandomGrid(9))
# print(areRowsValid(xGCD,yGCD,answer))



        
# def solveGrid(xAxis,yAxis,xDim,yDim):

#     return x


# print(concatinator([0,4,4,4,0]))
# printGrid(5,5,x)
# areRowsValid(yGCD,x)
# w= [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
# printGrid(9,9,w)

# def printGrid(x,y, array):
#     for i in range(x):
#         for j in range(y):
#             print(str(array[i][j])+"     ",end="")
#         print("\n")





# def GenSolve2(xGCD,yGCD,empty,rowsFilled=1,sizeRemaning=4):
#     listOfValids = []
#     if(rowsFilled==len(empty)):
#         print("valid")
#         print(empty)
#         return None
    
#     for i in range(len(empty)):
#         for x in itertools.product([0,i+1], repeat=sizeRemaning):
#                     temp = sizeRemaning
#                     while temp < 5:
#                         x = x+((empty[rowsFilled][temp]),)
#                         temp+=1
#                     if(isRowValid(x,yGCD[rowsFilled],traversedRows)):
#                         lastValue =i+1
#                         empty[rowsFilled] = x  
    
#     empty = np.transpose(empty)
#     index = len(empty)-rowsFilled-1
#     for x in itertools.product([0,lastValue], repeat=sizeRemaning):
#                     temp = 0
#                     while temp < rowsFilled:
#                         x = ((empty[index][temp]),)+x
#                         temp+=1
#                     if(isRowValid(x,xGCD[index],traversedRows)):
#                         empty[index] = x
#     empty = np.transpose(empty)
#     sizeRemaning-=1
#     rowsFilled+=1
#     print(empty)
#     GenSolve2(xGCD,yGCD,empty,rowsFilled,sizeRemaning)