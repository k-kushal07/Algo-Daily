def is_subseq(str1, str2):
    i,j = 0,0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i+=1
        j+=1
    return i == len(str1)

str1 = input('Enter the key string: ')
str2 = input('Enter the main string: ')
if is_subseq:
    print(str1+ ' is sub-sequence of '+ str2)
else:
    print(str1+ ' is not a sub-sequence of '+str2)
