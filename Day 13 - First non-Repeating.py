def non_repeating(string):
   chars = []
   count = {}
   
   for char in string:
      if char in count:
         count[char] += 1
      else:
         count[char] = 1
         chars.append(char)
         
   for char in chars:
      if count[char] == 1:
        return char
   return None

sentence = input('Enter the string: ')

if non_repeating(sentence):
    print(non_repeating(sentence) + 'is the first non repeating character.')
else:
    print('All the characters are repeating in the given sentence.')
