def min_array(arr, low, high): 
    if high < low: 
        return arr[0] 

    if high == low: 
        return arr[low] 
 
    mid = (low + high)//2 

    if mid < high and arr[mid+1] < arr[mid]: 
        return arr[mid+1] 

    if mid > low and arr[mid] < arr[mid - 1]: 
        return arr[mid] 
 
    if arr[high] > arr[mid]: 
        return findMin(arr, low, mid-1) 
    return findMin(arr, mid+1, high) 

arr = [int(ele) for ele in input().split()]
size = len(arr) 
print(min_array(arr, 0, size-1)) 
