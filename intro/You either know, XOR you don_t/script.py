from pwn import *
from  Crypto.Util.number import *
cipher="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
c=bytes.fromhex(cipher)
# flag= "crypto{".encode("utf-8")
key=b'myXORkey'
flag=xor(c,key)
print(flag)
# k=bytes_to_long(key)
# flag_filter=b"crypto{"
# while True:
#     k=k+1;
#     b=long_to_bytes(k)
#     result=xor(c,b)
#     if flag_filter in result:
#         print(result)
#         break