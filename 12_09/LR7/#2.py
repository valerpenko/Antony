str='Аргентина- манит негра'
str=str.replace(',','')
str=str.replace('.','')
str=str.replace('-','')
str=str.replace(':','')
str=str.replace(';','')
str=str.replace(' ','')
str=str.upper()
if str == str[::-1]:
    print(True)
else:
    print(False)