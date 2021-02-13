def missingPositive(arr):
    temp = 0
    n = len(arr)
    
    for i in range(n):
        if(arr[i] == 1):
            temp = 1
            break
    if temp == 0:
        return 1
    for i in range(n):
        if((arr[i] <= 0) or (arr[i] > n)):
            arr[i] = 1
    for i in range(n):
        arr[(arr[i] - 1) % n] += n
    for i in range(n):
        if(arr[i] <= n):
            return i+1
    return n+1

arr = [int(ele) for ele in input().split()]
print(missingPositive(arr))
