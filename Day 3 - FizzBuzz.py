def fizzbuzz(num):
    if(num==0):
        return ''
    else:
        if (num % 3 ==0 and num%5 == 0):
            return fizzbuzz(num-1) + 'fizzbuzz '
        elif (num % 5 == 0):
            return fizzbuzz(num-1) + 'buzz '
        elif (num % 3 == 0):
            return fizzbuzz(num-1) + 'fizz '
        else :
            return fizzbuzz(num-1) + (f'{num} ')

inp = int(input('Enter the number: '))    
print(fizzbuzz(inp))
