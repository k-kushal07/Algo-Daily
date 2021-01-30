def sub_finder(string, key):
	temp = 0
	for i in range(len(string)):
		if (temp == len(key)):
			break
		if (string[i] == key[temp]):
			temp += 1
		else:
			temp = 0
	
	if (temp < len(key)):
		return -1
	else:
	    return (i - temp)
	 
inp = input().lower()
val = input().lower()

print(sub_finder(inp, val))
