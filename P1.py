str = input("Enter string: ")
dct = {}
for i in str: 
 dct[i] = dct.get(i,0) + 1 
dct = sorted(dct.items(),key=lambda x: (-x[1],x[0])) 
for i in dct: 
    print(i[0],i[1])

