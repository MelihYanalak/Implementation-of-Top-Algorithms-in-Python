def sortByAscendingFinishTime(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i][1]>arr[i+1][1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
def optimalSymposium():
    symposiums = [[13,15],[11,12],[9,11],[11,14],[13,16],[15,17]]
    sortByAscendingFinishTime(symposiums)
    lastFinished = [-1,-1]
    solution = []
    for i in range(len(symposiums)):
        if symposiums[i][0] >= lastFinished[1]:
            solution.insert(len(solution),symposiums[i])
            lastFinished = symposiums[i]
    return solution

def planOfMinCost(m,opcosts):
    place = 0
    count = 0
    minsolution = []
    if opcosts[0][0] < opcosts[1][0]:
        place = 0
        count = count + opcosts[0][0]
        minsolution.insert(len(minsolution),"NY")
    else:
        place = 1
        count = count + opcosts[1][0]
        minsolution.insert(len(minsolution),"SF")
    for i in range(1,len(opcosts[0])):
        if place == 0:
            if opcosts[0][i] < opcosts[1][i] + m:
                count = count + opcosts[0][i]
                minsolution.insert(len(minsolution),"NY")
            else:
                place = 1
                count = count + opcosts[1][i] + m
                minsolution.insert(len(minsolution),"SF")
        else:
            if opcosts[1][i] < opcosts[0][i] + m:
                count = count + opcosts[1][i]
                minsolution.insert(len(minsolution),"SF")
            else:
                place = 0
                count = count + opcosts[0][i] + m
                minsolution.insert(len(minsolution),"NY")
    print("Optimum Solution is below with total cost %d" %(count))
    print(minsolution)


def sequence_align(x, y,gap,match,mismatch):
    A = [[None]*(len(y)) for i in range(len(x))]
    maxValue = -999999
    A[0][0] = 0
    for i in range(1,len(x)):
        A[i][0] = i * gap
    for j in range(1,len(y)):
        A[0][j] = j * gap
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if x[i-1] == y[j-1]:
                temp = match
            else:
                temp = mismatch
            A[i][j] = max(A[i][j-1] + gap,A[i-1][j] + gap,A[i-1][j-1] + temp)
            if A[i][j] >= maxValue:
                maxValue = A[i][j]
    return maxValue


    
def minOperation(arr):
    operation = [0]
    opNum = 0
    while (len(arr)>0):
        temp = findAndDeleteMin(arr)
        operation.insert(len(operation),operation[len(operation)-1]+temp)
    for i in range(0,len(operation)):
        opNum = opNum + operation[i]
    return [opNum,operation[len(operation)-1]]
def findAndDeleteMin(arr):
    min = [0,arr[0]]
    for i in range(1,len(arr)):
        if arr[i]< min[1] :
            min = [i,arr[i]]
    arr.pop(min[0])
    return (min[1])


def subArraySum(arr):
    sumNeg = 0
    sumPos = 0
    for i in range(0,len(arr)):
        if arr[i]<0:
            sumNeg = sumNeg + arr[i]
        else :
            sumPos = sumPos + arr[i]

    dpTable = [[None for i in range(sumPos-sumNeg+1)] for j in range(len(arr))]
    for i in range(0,len(arr)):
        for j in range(sumNeg,sumPos+1):
            if i == 0:
                dpTable[i][j-sumNeg] = (arr[i] == j)
            elif (sumNeg <= j - arr[i] and j - arr[i] <= sumPos):
                dpTable[i][j-sumNeg] = (arr[i] == j) or (dpTable[i-1][j - sumNeg]) or (dpTable[i-1][j - sumNeg - arr[i]])
                if (j == 0) and dpTable[i][j-sumNeg]:
                    return True
            else :
                dpTable[i][j - sumNeg] = (arr[i] == j) or (dpTable[i-1][j - sumNeg])
                if (j == 0) and dpTable[i][j-sumNeg]:
                    return True
    return False

def driverForPart1():
    opCosts = [[1,3,20,30],[50,20,2,4]]
    m = 10
    planOfMinCost(m,opCosts)

def driverForPart2():
    print("Optimal Symposium List is below:")
    print(optimalSymposium())

def driverForPart3():
    arr = [1,2,3,-3]
    print("Is there any subset with sum of 0 = %d" %(subArraySum(arr)))

def driverForPart4():
    print("String Alignment cost is %d" %(sequence_align("ALGORITMA","ALGORITHM",-1,2,-2)))

def driverForPart5():
    arr = [5,4,6,2,3,1]
    temp = minOperation(arr)
    print("Sum is: %d Operation Num is: %d" %(temp[1],temp[0]))
driverForPart1()
driverForPart2()
driverForPart3()
driverForPart4()
driverForPart5()