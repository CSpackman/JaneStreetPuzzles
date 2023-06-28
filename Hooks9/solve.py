import math
import matplotlib.pyplot as plt
from array import *
import numpy as np
import random
import itertools
answer = np.array([[0,4,4,4,0],[5,5,0,5,0],[3,0,0,5,4],[1,2,3,0,0],[2,0,3,5,0]])
xGCD = [0,1,1,5,4]
yGCD = [0,5,3,123,1]

xGCD9 = [5,1,6,1,8,1,22,7,8]
yGCD9 = [55,1,6,1,24,3,6,7,2]

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

def isRowValid(row,GCD):
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

def firstValids(xGCD,yGCD):
    listValids = []
    for i in range(5):
        for x in itertools.product([0,i+1], repeat=5):
            if(isRowValid(x,yGCD[0])):
                        empty  = np.zeros((5,5), dtype= int)
                        empty[0] = x
                        empty = np.transpose(empty)
                        copy = empty
                        for j in itertools.product([0,i+1], repeat=4):
                            temp =0
                            j =list(j)
                            j.insert(0,empty[0][temp])
                            if(isRowValid(j,xGCD[4])):
                                empty[4] = j
                                empty= np.transpose(empty)
                                listValids.append(empty)
                                empty= np.transpose(empty)
                                empty[4] = copy[4]


    return listValids

# valids = firstValids(xGCD,yGCD)

def generateFirstRowColPair(xGCD,yGCD,size):
    firstRowValids = set()
    firstColValids = set()
    lastRowValids = set()
    lastColValids = set()
    valids = []
    for x in range(size):
        for j in itertools.product([0,x+1], repeat=size):
                            if(isRowValid(j,yGCD[0])):
                                firstRowValids.add(j)
        for j in itertools.product([0,x+1], repeat=size):
                            if(isRowValid(j,xGCD[0])):
                                firstColValids.add(j)
        for j in itertools.product([0,x+1], repeat=size):
                            if(isRowValid(j,yGCD[size-1])):
                                lastRowValids.add(j)
        for j in itertools.product([0,x+1], repeat=size):
                            if(isRowValid(j,xGCD[size-1])):
                                lastColValids.add(j)      


        for i in firstRowValids:
            for j in firstColValids:
                if(i[0]==j[0]):
                    empty = np.zeros((size,size), dtype= int)
                    empty[0]= i
                    empty = np.transpose(empty)
                    empty[0] = j
                    empty = np.transpose(empty)
                    valids.append(empty)

        for i in firstRowValids:
            for j in lastColValids:
                if(i[0]==j[size-1]):
                    empty = np.zeros((size,size), dtype= int)
                    empty[0]= i
                    empty = np.transpose(empty)
                    empty[size-1] = j
                    empty = np.transpose(empty)
                    valids.append(empty)
        for i in lastRowValids:
            for j in firstColValids:
                if(i[size-1]==j[size-1]):
                    empty = np.zeros((size,size), dtype= int)
                    empty[size-1]= i
                    empty = np.transpose(empty)
                    empty[size-1] = j
                    empty = np.transpose(empty)
                    valids.append(empty)
        for i in lastRowValids:
            for j in lastColValids:
                if(i[size-1]==j[size-1]):
                    empty = np.zeros((size,size), dtype= int)
                    empty[size-1]= i
                    empty = np.transpose(empty)
                    empty[0] = j
                    empty = np.transpose(empty)
                    valids.append(empty)
        firstRowValids = set()
        firstColValids = set()
        lastRowValids = set()
        lastColValids = set()
    return valids

def nextSetOfValids(xGCD,yGCD,lastValid):
    valids = []
    firstRowValids = set()
    firstColValids = set()
    lastRowValids = set()
    lastColValids = set()

    size = len(lastValid[0]) #size of list
    nums_used = np.unique(lastValid.flatten())
    rowsColsLeft=size+1-len(nums_used) ## rowsColsLeft

    ## determines possible nums
    numsPossible = [x for x in range(size+1)] 
    for x in nums_used:
          numsPossible.remove(x)
    
    for digit in numsPossible:
        for j in itertools.product([0,digit], repeat=rowsColsLeft):
                            count =0
                            temp = list(j)
                            while rowsColsLeft+count < size:
                                temp.append(lastValid[size-rowsColsLeft][rowsColsLeft+count])
                                count+=1
                            if(isRowValid(temp,yGCD[size-rowsColsLeft])):
                                firstRowValids.add(j)
        lastValid = np.transpose(lastValid)
        for j in itertools.product([0,digit], repeat=rowsColsLeft):
                            temp = list(j)
                            count =0
                            while count <  5-rowsColsLeft:
                                temp.insert(count,lastValid[rowsColsLeft-1][count])
                                count+=1
                            if(isRowValid(temp,xGCD[0])):
                                firstColValids.add(j)
        lastValid = np.transpose(lastValid)

        for j in itertools.product([0,digit], repeat=rowsColsLeft):
                            temp = list(j)
                            count =0
                            while rowsColsLeft+count < 5:
                                temp.append(lastValid[0][rowsColsLeft+count])
                                count+=1
                            if(isRowValid(temp,yGCD[0])):
                                lastRowValids.add(j)

        lastValid = np.transpose(lastValid)
        for j in itertools.product([0,digit], repeat=rowsColsLeft):
                            temp = list(j)
                            count =0
                            while count < 5-rowsColsLeft:
                                temp.insert(count,lastValid[rowsColsLeft-1][count])
                                count+=1
                            if(isRowValid(temp,xGCD[rowsColsLeft-1])):
                                lastColValids.add(j)   
        lastValid = np.transpose(lastValid)
        for i in firstRowValids:
            for j in firstColValids:
                if(i[0]==j[0]):
                    empty = np.zeros((rowsColsLeft,rowsColsLeft), dtype= int)
                    empty[0]= i
                    empty = np.transpose(empty)
                    empty[0] = j
                    empty = np.transpose(empty)
                    valids.append(empty)

        for i in firstRowValids:
            for j in lastColValids:
                if(i[0]==j[rowsColsLeft-1]):
                    empty = np.zeros((rowsColsLeft,rowsColsLeft), dtype= int)
                    empty[0]= i
                    empty = np.transpose(empty)
                    empty[rowsColsLeft-1] = j
                    empty = np.transpose(empty)
                    valids.append(empty)
        for i in lastRowValids:
            for j in firstColValids:
                if(i[rowsColsLeft-1]==j[rowsColsLeft-1]):
                    empty = np.zeros((rowsColsLeft,rowsColsLeft), dtype= int)
                    empty[rowsColsLeft-1]= i
                    empty = np.transpose(empty)
                    empty[rowsColsLeft-1] = j
                    empty = np.transpose(empty)
                    valids.append(empty)
        for i in lastRowValids:
            for j in lastColValids:
                if(i[rowsColsLeft-1]==j[rowsColsLeft-1]):
                    empty = np.zeros((rowsColsLeft,rowsColsLeft), dtype= int)
                    empty[rowsColsLeft-1]= i
                    empty = np.transpose(empty)
                    empty[0] = j
                    empty = np.transpose(empty)
                    valids.append(empty)  


    return valids

def insert_at(big_arr, pos, to_insert_arr):
    x1 = pos[0]
    y1 = pos[1]
    x2 = x1 + to_insert_arr.shape[0]
    y2 = y1 + to_insert_arr.shape[1]

    assert x2 <= big_arr.shape[0], "the position will make the small matrix exceed the boundaries at x"
    assert y2 <= big_arr.shape[1], "the position will make the small matrix exceed the boundaries at y"

    big_arr[x1:x2, y1:y2] = to_insert_arr

    return big_arr
def solve(xGCD,yGCD,size):
    valids = generateFirstRowColPair(xGCD,yGCD,size)
    for one in valids:
        i = nextSetOfValids(xGCD,yGCD,one)
        # i =  insert_at(one,(1,0),i[0])
        for two in i:
            x = insert_at(one,(1,0),two)
            j = nextSetOfValids(xGCD,yGCD,x)
            for three in j:
                h = nextSetOfValids(xGCD,yGCD,three)
                return  h
            # return len(j)
        # insert_at(two,(1,0),j[0])

            #   for three in j:
            #         h = nextSetOfValids(xGCD,yGCD,three)
            #         return insert_at(three,(2,0),h)
        
print(solve(xGCD,yGCD,5))
# noDuplicates = set()
# for arr in valids:
#     noDuplicates.add(tuple(arr.flatten()))
# print("nine")
# print(len(noDuplicates))

# empty1 = np.zeros((5,5), dtype= int)
# empty1[0]=[0,4,4,4,0]
# empty1[1]=[0,0,0,0,0]
# empty1[2]=[0,0,0,0,4]
# empty1[3]=[0,0,0,0,0]
# empty1[4]=[0,0,0,0,0]

# x = nextSetOfValids(xGCD,yGCD,empty1)
# # print(x)
# noDuplicates = set()
# for arr in x:
#     noDuplicates.add(tuple(arr.flatten()))

# print(len(noDuplicates))

# empty2 = np.zeros((5,5), dtype= int)
# empty2[0]=[0,4,4,4,0]
# empty2[1]=[5,5,0,5,0]
# empty2[2]=[0,0,0,5,4]
# empty2[3]=[0,0,0,0,0]
# empty2[4]=[0,0,0,5,0]
# x = nextSetOfValids(xGCD,yGCD,empty2)
# # print(x)
# noDuplicates = set()
# for arr in x:
#     noDuplicates.add(tuple(arr.flatten()))

# print(len(noDuplicates))

# empty3 = np.zeros((5,5), dtype= int)
# empty3[0]=[0,4,4,4,0]
# empty3[1]=[5,5,0,5,0]
# empty3[2]=[3,0,0,5,4]
# empty3[3]=[0,0,3,0,0]
# empty3[4]=[0,0,3,5,0]
# x = nextSetOfValids(xGCD,yGCD,empty3)
# # print(x)
# noDuplicates = set()
# for arr in x:
#     noDuplicates.add(tuple(arr.flatten()))

# print(len(noDuplicates))

# i = np.zeros((2,2), dtype= int)

# i[0]=[0,0]
# i[1]=[0,0]
# noDuplicates = set()
# for arr in x:
#     noDuplicates.add(tuple(arr.flatten()))

# print(len(noDuplicates))

# empty4 = np.zeros((5,5), dtype= int)
# empty4[0]=[0,4,4,4,0]
# empty4[1]=[5,5,0,5,0]
# empty4[2]=[3,0,0,5,4]
# empty4[3]=[0,2,3,0,0]
# empty4[4]=[2,0,3,5,0]
# x = nextSetOfValids(xGCD,yGCD,empty4)
# noDuplicates = set()
# for arr in x:
#     noDuplicates.add(tuple(arr.flatten()))
# print(len(noDuplicates))

# empty1 = np.zeros((5,5), dtype= int)
# empty1[0]=[0,4,4,4,0]
# empty1[1]=[0,0,0,0,0]
# empty1[2]=[0,0,0,0,4]
# empty1[3]=[0,0,0,0,0]
# empty1[4]=[0,0,0,0,0]

# empty2 = np.zeros((4,4), dtype= int)
# empty2[0]=[5,5,0,5]
# empty2[1]=[0,0,0,5]
# empty2[2]=[0,0,0,0]
# empty2[3]=[0,0,0,5]

# empty3 = np.zeros((3,3), dtype= int)
# empty3[0]=[3,0,0]
# empty3[1]=[0,0,3]
# empty3[2]=[0,0,3]

# x= insert_at(empty1,(1,0),empty2)
# y= insert_at(x,(2,0),empty3)
# print(y)

# def solvePuzzle(xGCD,yGCD, current, traversing=[]):
#     traversing2 = nextSetOfValids(xGCD,yGCD,current)
#     for second in traversing2:
#         current=insert_at(current,(1,0),second)
#         traversing3 = nextSetOfValids(xGCD,yGCD,current)
#         for third in traversing3:
#             current=insert_at(current,(1,0),third)
#             # traversing4 = nextSetOfValids(xGCD,yGCD,current)
#             print(current)

#     try:
#         x=insert_at(current,(1,0),traversing[0])
#         print(traversing[3])
#     except:
#           print(x)
#           return x
#     print(x)
#     return False
# solvePuzzle(xGCD,yGCD,empty)

      

# for x in valids:
#     # for i in firstRowValids:
#     print(x,end="\n \n")
#         # if(np.array_equiv(x,i)):
#         #     count+=1
#         # if(x==i):
#         #        print(x,i)
#         #        count+=1
# x = generateFirstRowColPair(xGCD,yGCD,5)
# print(x)
# print(len(x))
# empty = np.zeros((5,5), dtype= int)
# empty[0]=[0,4,4,4,0]
# empty[1]=[0,0,0,0,0]
# empty[2]=[0,0,0,0,4]
# empty[3]=[0,0,0,0,0]
# empty[4]=[0,0,0,0,0]

# for i in x:
#        if(np.array_equiv(i,empty)):
#             print("yay")

# xGCD = [5,1,6,1,8,1,22,7,8]
# yGCD = [55,1,6,1,24,3,6,7,2]
# x = generateFirstRowColPair(xGCD,yGCD,5)
# print(x)
# print(len(x))
# empty = np.zeros((5,5), dtype= int)
# empty[0]=[0,4,4,4,0]
# empty[1]=[0,0,0,0,0]
# empty[2]=[0,0,0,0,4]
# empty[3]=[0,0,0,0,0]
# empty[4]=[0,0,0,0,0]
# count = 0
# for i in x:
#        for j in x:
#         if(np.array_equiv(i,j)):
#             count+=1
# print(count)


# empty = np.zeros((5,5), dtype= int)
# empty[0]=[0,4,4,4,0]
# empty[1]=[5,5,0,5,0]
# empty[2]=[3,0,0,5,4]
# empty[3]=[0,0,3,0,0]
# empty[4]=[0,0,3,5,0]

# y= nextSetOfValids(xGCD,yGCD,empty)

# empty = np.zeros((5,5), dtype= int)
# empty[0]=[0,4,4,4,0]
# empty[1]=[5,5,0,5,0]
# empty[2]=[0,0,0,5,4]
# empty[3]=[0,0,0,0,0]
# empty[4]=[0,0,0,5,0]

# y= nextSetOfValids(xGCD,yGCD,empty)

# empty = np.zeros((5,5), dtype= int)
# empty[0]=[0,4,4,4,0]
# empty[1]=[0,0,0,0,0]
# empty[2]=[0,0,0,0,4]
# empty[3]=[0,0,0,0,0]
# empty[4]=[0,0,0,0,0]

# y= nextSetOfValids(xGCD,yGCD,empty)

# print(y)
# print(len(y))
# empty = np.zeros((4,4), dtype= int)
# empty[0]=[5,5,0,5]
# empty[1]=[0,0,0,5]
# empty[2]=[0,0,0,0]
# empty[3]=[0,0,0,5]

# for i in y:
#     if(np.array_equiv(i,empty)):
#            print("yay")