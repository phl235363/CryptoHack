def powmod(a,n,p):
    if n==1:
        return a%p
    if n==0:
        return 1
    a=a%p
    tmp=1
    while n>1:
        if n%2==0:
            a=(a*a)%p
            n=n/2
        else :
            tmp=a
            a=(a*a)%p
            n=(n-1)/2
    return (a*tmp)%p
#a^p-1 mod p =1 => a^-1 mod p = a^ p-2 mod p
print(powmod(3,11,13))