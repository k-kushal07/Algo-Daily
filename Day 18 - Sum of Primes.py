n = 100000
dp = [0] * (n + 1)

def main():
    array = [0] * (n + 1)

    array[0] = 1
    array[1] = 1

    for i in range(2, int(n**(1/2) + 1)):
        if array[i] == 0:
            for j in range(i * i, n + 1, i):
                array[j] = 1
    curr_sum = 0

    for i in range(1, n + 1):
        if array[i] == 0:
            curr_sum += i
        dp[i] = curr_sum

num = int(input('Enter the number: '))
main()
print(dp[num])
