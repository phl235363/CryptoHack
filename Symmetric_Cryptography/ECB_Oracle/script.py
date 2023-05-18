import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding  import pad     , unpad
def string2hex(data = ""):
    byte=data.encode("utf-8")
    datahex=byte.hex()
    return datahex

URL="http://aes.cryptohack.org/ecb_oracle/encrypt/"
ALPHABET = 'abcdefghijklmnopqrstuvwxyz0123456789_\{\}'
s=requests.session()
def encrypt(data):
    tmp=string2hex(data)

    r = s.get(f"http://aes.cryptohack.org/ecb_oracle/encrypt/{tmp}/")
    result=r.json()["ciphertext"]
    return result

def getciphertext():
    result=[]
    for i in range(0,26):#25 is flag len 
        if (i<16):
            padding= "A"*(16-i)
            result.append(encrypt(padding)[0:32])
        else:
            padding="A"*(32 -i)
            result.append(encrypt(padding)[32:64])

  

    return result

# 41414141414141414141414141414141

def decrypt():
    temp=0
    cipher=getciphertext()
    flag=""
    print(cipher[16])
    for i in range  (1,26):
        ciphertext=cipher[i]

        print(i)
        if i < 16:
            for letter in ALPHABET:
                coutn=16-len(flag)-1
                data="A"*coutn+flag+letter
                re=encrypt(data)
                if ciphertext in re:
                    flag=flag+letter
                    print(flag)
                    break
        
        else:
            for letter in ALPHABET:
                data=flag[-15:]+letter

                re=encrypt(data=data)
                if ciphertext in re[0:32]:
                    flag=flag+letter
                    print(flag)
                    break

decrypt()
# test="crypto{p3n6u1n5_"
# hexstr=string2hex(test)

# cipher=getciphertext()

# print(cipher[16])
# result=encrypt(test)
# print("encode test: "+result)


