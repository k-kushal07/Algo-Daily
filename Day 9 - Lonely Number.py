def lonely_num(lst):
        temp=0
        for n in lst:
            temp ^= n
        return temp
        
inp = [int(ele) for ele in input().split()]
print(lonely_num(inp))
