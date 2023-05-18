e=65537
p=17
q=23
n=p*q
phin=(p-1)*(q-1)
plain=12
cipher = pow (plain , e, n)
print (cipher)