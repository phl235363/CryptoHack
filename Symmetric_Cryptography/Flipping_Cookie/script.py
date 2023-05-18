import requests
from Crypto.Cipher import AES
import os
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta
from pwn import xor 
URL="https://aes.cryptohack.org/flipping_cookie/"
def get_request():
    s=requests.session()
    path=URL+"get_cookie/"
    result=s.get(path)
    return  result.json()["cookie"]

def get_flag(iv, cookie):
    s=requests.session()
    path=URL + f"check_admin/{cookie}/{iv}/"
    result=s.get(path)
    return result.json()







#b'admin=False;expiry=1684084472\x03\x03\x03'

#plain = dec(cipher) ^ iv 
#dec(cipher) = #plain ^ iv
#fakeplain= dec(cipher) ^ fakeiv
#fakeiv = fakeplain ^ dec(cipher) = fakeplain ^ plain ^ iv

response=get_request()
iv=response[0:32]
block1=response[32:64]
block2=response[64:96]
ciphertext=block1+block2
print("IV = " +  iv)

print("ciphertext = " + block1+block2)
plain =     b'admin=False;expi'
fakeplain = b';admin=True;expi' 
ivbyte=bytes.fromhex(iv)
fakeivbyte=xor(xor(fakeplain,plain),ivbyte)
fakeiv=fakeivbyte.hex()
flag= get_flag(fakeiv ,ciphertext)
print(flag)



