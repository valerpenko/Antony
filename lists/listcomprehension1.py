#a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#l=[a[i:i+13] for i in range(0,14,13) for j in range(0,1)]
#=[a[i:i+13] for i in range(0,14,13)]
l=[ [chr(ord('a')+j*13+i) for i in range(0,13)] for j in range(0,2)]
print(l)
