def subArraySum(arr, n, key): 
	curr_sum = arr[0] 
	start = 0

	i = 1
	while i <= n: 
		while curr_sum > sum and start < i-1: 
			curr_sum = curr_sum - arr[start] 
			start += 1
			
		if curr_sum == sum: 
			return 1

		if i < n: 
			curr_sum = curr_sum + arr[i] 
		i += 1

	return 0

# Driver program 
arr = [int(ele) for ele in input().split()] 
n = len(arr)
key = int(input())

if subArraySum(arr, n, key):
    print('Yes there is a subarray that sums up to', key)
else:
    print('No subarray')

# This code is Contributed by shreyanshi_arun. 
