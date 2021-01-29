def sum_digits(num): 
    if num == 0: 
        return 0
    elif num % 9 == 0: 
        return 9 
    else: 
        return (num % 9) 
  
number = int(input('Enter the number: '))
print(sum_digits(number))
