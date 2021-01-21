def reverse_alpha(string):
    
    newList = list(string)
    
    rightptr = len(newList)-1
    leftptr = 0
    
    while leftptr < rightptr:
        if not newList[leftptr].isalpha():
            leftptr +=1
        elif not newList[rightptr].isalpha():
            rightptr -=1
        else:
            newList[leftptr], newList[rightptr] = newList[rightptr], newList[leftptr]
            
            leftptr +=1
            rightptr -=1
    
    return ''.join(newList)
    
inp = input()
print(reverse_alpha(inp))
