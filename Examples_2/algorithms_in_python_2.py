arr = [[37,23,22,32], [21,6,7,10], [53,34,30,31],[32,13,9,6],[43,21,15,8]]

def specialArray(arr):
    count = 0
    for i in range(len(arr)-1):
        for j in range(len(arr[0])-1):
            if(arr[i][j]+arr[i+1][j+1] > arr[i][j+1]+arr[i+1][j]):
                count = count + 1
                x = arr[i][j]+arr[i+1][j+1]
                y = arr[i][j+1]+arr[i+1][j]
                arr[i][j+1] = arr[i][j+1]+x-y
    if(count == 1):
        printArr(arr)
    elif(count == 0):
       print("Array is already special")
    else:
        print("It requires more than 1 change")


def getLeftMostMin(arr):
    min = arr[0]
    minIndex = 0
    for i in range(1, len(arr)):
        if(arr[i] < min):
            min = arr[i]
            minIndex = i
    return minIndex

def findMinimums(arr,start,end,index):
    if (start == end):
        index[start] = getLeftMostMin(arr[start])
    else:
        if((end-start)%2==0):
            mid = (end-start)//2
            findMinimums(arr, start, mid-1, index)
            findMinimums(arr, mid, mid,index)
            findMinimums(arr, mid+1, end, index)
        else:
            mid = ((end-start)//2)+start
            findMinimums(arr, start, mid, index)
            findMinimums(arr, mid+1, end, index)

def minRow(arr):
    index = []
    for i in range(len(arr)):
        index.append(0)
    findMinimums(arr, 0, len(arr)-1, index)
    return index

def printArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print ("%2d" %(arr[i][j]), end=" ")
        print()



def optimalDayHelper(A,B,index):
   if (len(A) == 1):
      return [B[0]-A[0],index]
   if (len(A) > 1):
      k = len(A)//2
      x = optimalDayHelper(A[0:k],B[0:k],k)
      y = optimalDayHelper(A[k:2*k],B[k:2*k],2*k)
      return compareAndMerge(x,y)
def compareAndMerge(x,y):
   if x[0] < y[0]:
      return y
   else:
      return x

def optimalDay(A,B):
   A = A[:-1]
   B = B[1:]
   size = len(A)
   tempA = A
   tempB = B
   flag = False
   if len(A)%2 == 1:
      flag = True
      A = A[:-1]
      B = B[:-1]
   result = optimalDayHelper(A,B,len(A))
   if result[0] < 1:
      print("There is no day to make money")
      return [0,0]
   if flag == True:
      if (tempB[size-1]-tempA[size-1]) > result[0]:
         return [(tempB[size-1]-tempA[size-1]),size]

   return result


def maxCrossingSum(arr, l, m, h) : 
    sm = 0; left_sum = -10000
    for i in range(m, l-1, -1) : 
        sm = sm + arr[i] 
        if (sm > left_sum) : 
            left_sum = sm 
    sm = 0; right_sum = -1000
    for i in range(m + 1, h + 1) : 
        sm = sm + arr[i] 
        if (sm > right_sum) : 
            right_sum = sm 
    return left_sum + right_sum
def maxSubArraySumHelper(arr, l, h) : 
    if (l == h) : 
        return arr[l] 
    m = (l + h) // 2
    return max(maxSubArraySumHelper(arr, l, m), maxSubArraySumHelper(arr, m+1, h), maxCrossingSum(arr, l, m, h))
def maxSubArraySum(arr):
   n = len(arr) 
   return maxSubArraySumHelper(arr, 0, n-1)

def colorGraph(G, color, pos, c):  
      
    if color[pos] != -1 and color[pos] != c:  
        return False 
    color[pos] = c  
    ans = True 
    for i in range(0, len(G)):  
        if G[pos][i]:  
            if color[i] == -1:  
                ans &= colorGraph(G, color, i, 1-c)  
                  
            if color[i] !=-1 and color[i] != 1-c:  
                return False 
        if not ans:  
            return False 
    return True 
def isBipartite(G):  
    color = [-1] * len(G) 
    pos = 0 
    return colorGraph(G, color, pos, 1)


def kthlargest(arr1, arr2, k):
    if len(arr1) == 0:
        return arr2[k]
    elif len(arr2) == 0:
        return arr1[k]

    mida1 = int(len(arr1)/2)
    mida2 = int(len(arr2)/2)
    if mida1+mida2<k:
        if arr1[mida1]>arr2[mida2]:
            return kthlargest(arr1, arr2[mida2+1:], k-mida2-1)
        else:
            return kthlargest(arr1[mida1+1:], arr2, k-mida1-1)
    else:
        if arr1[mida1]>arr2[mida2]:
            return kthlargest(arr1[:mida1], arr2, k)
        else:
            return kthlargest(arr1, arr2[:mida2], k)

def driverForPart1():
    print("NOT SPECIAL ARRAY")
    printArr(arr)
    print("INDEXES OF MINIMUM ELEMENT IN EACH ROW")
    print (minRow(arr))
    print("ARRAY CHANGED TO SPECIAL")
    specialArray(arr)
def driverForPart2():
   arr1 = [2, 3, 6, 7, 9] 
   arr2 = [1, 4, 8, 10]
   k = 4
   print("%dth largest number is:"%(k))
   print(kthlargest(arr1,arr2,k-1))
def driverForPart3():   
   A = [5, -6, 6, 7, -6, 7, -4, 3]
   print("Maximum contiguous subset sum is :")
   print(maxSubArraySum(A))
def driverForPart4():   
   G = [[0, 1, 0, 1],   [1, 0, 1, 0],  [0, 1, 0, 1], [1, 0, 1, 0]]  
   print("Is the graph bipartite:")
   if isBipartite(G):
      print("Yes")  
   else: 
      print("No")
def driverForPart5():
   A = [5,11,2,21,5,7,8,12,13,None]
   B = [None,7,9,5,21,7,13,10,14,20]
   result = optimalDay(A,B)
   print("Day number %d is the best option with gain = %d" %(result[1],result[0]))

driverForPart1()
driverForPart2()
driverForPart3()
driverForPart4()
driverForPart5()
