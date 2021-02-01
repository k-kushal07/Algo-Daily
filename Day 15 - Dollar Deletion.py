def dollarDelete(string): 
    st = [] 
    for i in string: 
        if i=='$' :
            st.pop()
            continue
        st.append(i)
    return ''.join(st) 


def compare(str1, str2):
    if(dollarDelete(str1) == dollarDelete(str2)):
        print('The strings are same after deletion of Dollar sign')
    else:
        print('The strings are different even after deletion')

str1, str2 = input('Enter the strings to be compared: ').split()
compare(str1, str2)
