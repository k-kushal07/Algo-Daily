def maxOfMin(arr, n) : 
	arr.sort()
	sm = 0
	for i in range(0, n - 1, 2): 
		sm += arr[i]
	return sm

array = [int(ele) for ele in input('Enter the array elements: ').split()]
size = len(array)

print(maxOfMin(array, size))
