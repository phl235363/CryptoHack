import requests
from Crypto.Util.number import *
from pwn import *
URL="https://aes.cryptohack.org/bean_counter/encrypt/"
def encrypt():
    s=requests.session()
    result=s.get(URL).json()["encrypted"]
    return result

# print(len(response))
# print((28534/2)/16)
# #28534 hex
# #14267.0 byte
# test="a"
# test.zfill(5)
# print(test.zfill(5))
def encrypt():
    url = "http://aes.cryptohack.org/bean_counter/encrypt/"
    rsp = requests.get(url)
    return rsp.json()['encrypted']

png_hdr = bytes([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 0x00, 0x0d, 0x49, 0x48, 0x44, 0x52])
encrypted = bytes.fromhex(encrypt())

keystream = []
for i in range(len(png_hdr)):
    keystream.append(png_hdr[i] ^ encrypted[i])

print(keystream)

png = [0]*len(encrypted)
for i in range(len(encrypted)):
    png[i] = encrypted[i] ^ keystream[i%len(keystream)]

with open('bean_counter.png', 'wb') as fd:
    fd.write(bytes(png))


