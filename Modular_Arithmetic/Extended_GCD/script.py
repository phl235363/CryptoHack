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
    
def EGDC(a,b):
    xa=1
    ya=0
    xb=0
    yb=1
    while b!=0:
        q=a//b
        r=a%b
        a=b
        b=r
        xr=xa-q*xb
        yr=ya-q*yb
        xa=xb
        ya=yb
        xb=xr
        yb=yr
    return (xa,ya)






    
result=EGDC(26513,32321)
print(result)
print(GCD(result[0],result[1]))
