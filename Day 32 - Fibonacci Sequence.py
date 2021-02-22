def fibo(num): 
    a = 0
    b = 1
    if(num < 0): 
        print("Invalid Number") 
    elif(num == 0): 
        return a 
    elif(num == 1): 
        return b 
    else: 
        for i in range(2,num+1): 
            c = a + b 
            a = b 
            b = c 
        return b 

num = int(input('Enter the number: '))
print(fibo(num))
