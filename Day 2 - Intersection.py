def intersect(lst1, lst2):
    return [value for value in lst1 if value in lst2]

inp1 = [int(item) for item in input("Enter the items of First list: ").split()] 
inp2 = [int(item) for item in input("Enter the items of Second list: ").split()] 
print(list(set(intersect(inp1, inp2))))
