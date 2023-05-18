import requests
from Crypto.Util.number import *
from pwn import xor
URL="https://aes.cryptohack.org/ecbcbcwtf/"

def get_request():
    s=requests.session()
    result=s.get(URL+"encrypt_flag/")
    return result.json()["ciphertext"]
def decrypt(cipher):
    s=requests.session()
    result=s.get(URL+"decrypt/"+cipher+"/")
    return result.json()["plaintext"]
data=get_request()
print(data)

iv=data[0:32]
ciphertext1=data[32:64]
ciphertext2=data[64:96]
print("IV = "+iv)
print("Ciphertext1 = "+ciphertext1)
print("Ciphertext2 = "+ciphertext2)
plain2=decrypt(ciphertext2)
plain2=bytes.fromhex(plain2)
flagbyte2=xor(plain2, bytes.fromhex( ciphertext1))
plain1=decrypt(ciphertext1)
plain1=bytes.fromhex(plain1)
iv=bytes.fromhex(iv)
flagbyte1=xor(plain1,iv)
print(flagbyte1+flagbyte2)



#crypto{3cb_5uck5


