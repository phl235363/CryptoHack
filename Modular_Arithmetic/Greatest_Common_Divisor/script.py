def GCD(a,b):
    if a<b:
        tmp =a
        a=b
        b=tmp
   
    while a%b!= 0:
        tmp=b
        b=a%b
        a=tmp
    return b
    
a = 66528
b = 52920
print(GCD(a,b))