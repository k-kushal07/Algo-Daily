def missingNumber(arr, n):
    actual_sum = (n + 1)*(n + 2)//2
    current_sum = sum(arr)
    
    return actual_sum - current_sum

array = [int(ele) for ele in input('Enter the array elements: ').split()]
n = len(array) 

print(missingNumber(array, n))
