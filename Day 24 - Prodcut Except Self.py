def productExceptSelf(lst):
    product = 1
    newlst = []
    for i in lst:
        product*=i  
    for element in lst:
        newlst.append(product//element)
    return newlst
    
inputList = [int(item) for item in input().split()]

print(productExceptSelf(inputList))
