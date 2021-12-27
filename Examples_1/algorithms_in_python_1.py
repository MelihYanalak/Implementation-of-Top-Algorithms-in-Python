minProduct = 99999999999999999999999
resultArray = []
countInsertion = 0
countQuick = 0

def alternateBoxes(arr):
    x = int(len(arr)/2)
    y = int(len(arr))
    for i in range(1,x,2):
        temp = arr[i]
        arr[i] = arr[y-i-1]
        arr[y-i-1] = temp


def fakeCoin(arr):
    n = len(arr)
    if n==1:
        return (arr[0])
    else:
        if n%3==1:
            if arr[n-1]<arr[0]:
                return (arr[n-1])
        if n%3==2:
            if arr[n-1]<arr[0]:
                return (arr[n-1])
            if arr[n-2]<arr[0]:
                return (arr[n-2])
        x = int(len(arr)/3)
        a = arr[0:x]
        b = arr[x:(2*x)]
        c = arr[(2*x):(3*x)]
        if calculateSumOfArray(a) < calculateSumOfArray(b):
            return fakeCoin(a)
        if calculateSumOfArray(b) < calculateSumOfArray(a):
            return fakeCoin(b)
        if calculateSumOfArray(b) == calculateSumOfArray(a):
            return fakeCoin(c)
def calculateSumOfArray(arr):
    sum = 0
    for x in range(len(arr)):
        sum += arr[x]
    return sum
def calculateMultOfArray(arr):
    sum = 1
    for x in range(len(arr)):
        sum *= arr[x]
    return sum
def insertionSort(arr):
    global countInsertion
    for i in range(len(arr)):
        v = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > v):
            countInsertion = countInsertion + 1
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = v
def quickSort(arr,left,right):
    if left < right:
        s = hoarePartition(arr,left,right)
        quickSort(arr,left,s-1)
        quickSort(arr,s+1,right)
    else:
        return


def hoarePartition(arr,left,right):
    global countQuick
    p = arr[left]
    i = left
    j = right
    while j > i:
        while arr[i] < p:
            i = i + 1
        while arr[j] > p:
            j = j - 1
        countQuick = countQuick + 1
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    countQuick = countQuick + 1
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
    return j
def findMedian(arr):
    return quickSelect(arr,0,len(arr)-1,int(len(arr)/2)+1)
def quickSelect(arr,left,right,k):
    s = lomutoPartition(arr,left,right)
    if s-left == k-1:
        return arr[s]
    if s-left > (k-1):
        return quickSelect(arr,left,s-1,k)
    else:
        return quickSelect(arr,s+1,right,k-1+left-s)
def lomutoPartition(arr,left,right):
    p = arr[left]
    s = left
    for i in range(left+1,right+1,1):
        if arr[i]<p:
            s = s+1
            temp = arr[i]
            arr[i] = arr[s]
            arr[s] = temp
    temp = arr[left]
    arr[left] = arr[s]
    arr[s] = temp
    return s
def optimalSubset(str1, index, curr,cmpValue): 
    n = len(str1) 
  
    if (index == n): 
        return
    global minProduct
    global resultArray
    
    if calculateSumOfArray(curr) >= cmpValue :
        if calculateMultOfArray(curr) < minProduct:
            minProduct = calculateMultOfArray(curr)
            resultArray.clear()
            resultArray.extend(curr)

   
    for i in range(index + 1, n): 
        curr.append(str1[i]) 
        optimalSubset(str1, i, curr,cmpValue) 
  
      
        value = curr.pop(len(curr)-1)
    return
def findMax(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
def findMin(arr):
    min = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

    
def driverForPart1():
    arr = ["black","black","black","black","black","white","white","white","white","white"]
    alternateBoxes(arr)
    print(arr)


def driverForPart2():
    arr = [2,2,1,2,2,2,2,2,2,2,2,2,2,2,2]
    arr2 = [3,3,3,3,3,3,3,2]
    print("Fake coin is = ")
    print(fakeCoin(arr))
    print("Fake coin is = ")
    print(fakeCoin(arr2))


def driverForPart3():
    arr = [1,5,9,2,12,3,7,6,14,13,11,8,4,10]
    arr2 = [1,5,9,2,12,3,7,6,14,13,11,8,4,10]
    print("before sort: ")
    print(arr)
    insertionSort(arr)
    quickSort(arr2,0,len(arr2)-1)
    print("after sort: ")
    print(arr)
    print("number of swap operations for insertion sort = ")
    print(countInsertion)
    print("number of swap operations for quicksort = ")
    print(countQuick)


def driverForPart4():
    arr = [5,2,4,7,3,1,6]
    print("Median is = ")
    print(findMedian(arr))


def driverForPart5():
    arr = [2,4,7,5,22,11] 
    arr2 = []
    cmpValue = (findMax(arr)+findMin(arr))*float(len(arr)/4)
    optimalSubset(arr, -1, arr2,cmpValue)
    print("optimal subset is = ")
    print(resultArray)
# Driver code 


driverForPart1()
driverForPart2()
driverForPart3()
driverForPart4()
driverForPart5()

