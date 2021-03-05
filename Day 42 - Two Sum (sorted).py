def two_sum(arr, key):
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] + arr[right] == key:
                return [left+1, right+1]
            elif arr[left] + arr[right] > key:
                right -= 1
            elif arr[left] + arr[right] < key:
                left += 1
                
inpArray = [int(ele) for ele in input('Enter the array elements: ').split()]
key = int(input('Enter the target value: '))
print(two_sum(inpArray, key))
