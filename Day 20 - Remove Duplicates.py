def rem_duplicate(arr): 
    d = {i : 0 for i in arr} 

    for i in range(len(arr)):
            d[arr[i]] = 1

arr =  [int(ele) for ele in input().split()]
size = len(arr) 

print(rem_duplicate(arr))
