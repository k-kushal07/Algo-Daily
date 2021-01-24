def majority_finder(arr, size):
    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    count = 0
    for key in arr:
        if d[key] > size//2:
            count = 1
            return key
    return -1
    
inp = [int(ele) for ele in input('Enter the list: ').split()]

majority = majority_finder(inp, len(inp))
if(majority > 0):
    print('The majority element is ', majority)
else:
    print('There is no majority element')
