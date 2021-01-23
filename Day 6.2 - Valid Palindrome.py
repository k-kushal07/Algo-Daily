def palindrome(line):
    start, end = 0, len(line)-1
    while start < end:
        if line[start].isalnum() and line[end].isalnum():
            if line[start].lower() == line[end].lower():
                start += 1
                end -= 1
            else:
                return False
        else:
            if not line[start].isalnum():
                start += 1
            if not line[end].isalnum():
                end -= 1
    return True
    
inp = input('Enter the sentence: ')
if palindrome(inp):
    print('Palindrome')
else:
    print('Not a Palindrome')
