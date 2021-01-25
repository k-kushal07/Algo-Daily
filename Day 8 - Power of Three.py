def power_of_three(num):
    if num%3 == 0:
        return power_of_three(num/3)
    return num==1
        
inp = int(input('Enter the value: '))
print(power_of_three(inp))
