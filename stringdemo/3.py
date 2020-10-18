x = input()
s=x
s = s.replace('a', '')
s = s.replace('o', '')
s = s.replace('y', '')
s = s.replace('e', '')
s = s.replace('u', '')
s = s.replace('i', '')
s = s.replace('A', '')
s = s.replace('O', '')
s = s.replace('Y', '')
s = s.replace('E', '')
s = s.replace('U', '')
s = s.replace('I', '')
print(s)
s=x
vowels=['a','e','y']
for i in range(0,len(vowels)):
    s = s.replace(vowels[i],'')
print(s)
s=x
vowels=['a','e','y']
for vowel in vowels:
    s = s.replace(vowel,'')
print(s)
