def sumPair(arr, key):
    s = set()
    for i in range(0, len(arr)):
        temp = key - arr[i]
        if (temp in s):
            return (temp, arr[i])
        s.add(arr[i])

inpArr = [int(ele) for ele in input('Enter the array element: ').split()]
key = int(input('Enter the key value: '))
print(f'The pair that evaluates to {key} is {sumPair(inpArr, key)}')
