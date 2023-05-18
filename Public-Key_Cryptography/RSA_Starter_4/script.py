#d*e mod n  =1 
#d=e^-1 mod n
#e^phin mod n =1 
#e^phin -1 = e ^-1 mod n 
p = 857504083339712752489993810777

q = 1029224947942998075080348647219
n=p*q
e=65537
phi = (p-1)*(q-1)                        #totient of n
d = pow(e, -1, phi)                      
print( d)