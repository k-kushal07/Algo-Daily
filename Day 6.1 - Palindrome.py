def palindrome(word):
    return word == word[::-1]
    
inp = input('Enter the word: ')
if palindrome(inp):
    print('Palindrome')
else:
    print('Not a Palindrome')
