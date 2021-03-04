def shortestPalindrome(string):
    if string=="":
        return string
    pattern = string + string[::-1] 
    prefix = [-1] * len(pattern)
    j = -1
    for i in range(1, len(pattern)):
        while j>-1 and pattern[j+1]!=pattern[i]:
            j = prefix[j]
        j += 1
        prefix[i] = j
    i = prefix[-1]
    while i >= len(string):
        i = prefix[i]
    return string[i+1:][::-1] + string

inp = input('Enter the string')
print(shortestPalindrome(inp))
