import pipes
print ('скопируйте фрагмент файла в буферобмена')
s=pyperclip.paste()
s=s.replace('\n','')
n= len(s)
s1=s.replace(' ','')
n1=len(s1)
print (" количество символов спробелами", str(n),sep='--->')
print (" количество символов без пробелов",str(n1), sep='--->')