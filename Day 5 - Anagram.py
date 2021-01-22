def anagram(str1, str2):
    if(len(str1) != len(str2)):
        return False
    count = 0
    
    for i in str1:
        count += ord(i)
    for i in str2:
        count -= ord(i)
        
    return (count==0)
    
input1, input2, *rest = [word for word in input('Enter the strings to compare: ').split()]

print(input1)
print(input2)

if anagram(input1, input2):
    print('Yes, the strings are anagram of each other.')
else:
    print('No, the strings are not anagram.')
