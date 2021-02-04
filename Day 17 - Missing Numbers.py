def missingNumbers(arr, n): 
    b = [0] * (arr[n - 1] + 1) 
 
    for i in range(n): 
        b[arr[i]] = 1

    missing = [i for i in range(arr[0], arr[n - 1] + 1) if b[i] == 0]
    
    return missing

array = [int(ele) for ele in input('Enter the array elements: ').split()]
n = len(array) 

print(missingNumbers(array, n))
