#a^p-1 mod p =1 => a^-1 mod p = a^ p-2 mod p


def inversemod(a,p):
    return pow( a,p-2,p)

def Chinese_Remainder(a,m):
    k=len(a)
    M=1
    for item in m:
        M=M*item
    Mi=[]
    for i in range (0,k):
        Mi.append(M//m[i])
    
    y=[]
    for i in range (0,k):
        
        y.append(inversemod(Mi[i],m[i]))
    result =0
    for i in range (0,k):
        result += a[i]*Mi[i]*y[i]
    return result%M


a=[2,3,5]
m=[5,11,17]
print(Chinese_Remainder(a,m))
# M=11*17
# print(inversemod(M,5))
