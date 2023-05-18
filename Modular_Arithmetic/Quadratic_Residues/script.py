p=29
ints=  [14,6,11]
list=[]
for item in range(p):
    if (pow(item , 2 , p ) in ints ):
        list.append(item)

print (min(list))