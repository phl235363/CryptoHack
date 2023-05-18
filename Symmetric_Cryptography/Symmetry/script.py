import requests
URL="https://aes.cryptohack.org/symmetry/"
def encrypt(plaintext, iv ):
    s= requests.session()
    path = URL + f"encrypt/{plaintext}/{iv}/"
    result= s.get(path).json()["ciphertext"]
    return result
def encrypt_flag():
    s=requests.session()
    path= URL + "encrypt_flag/"
    result = s.get(path).json()["ciphertext"]
    print(result)
    return result


response = encrypt_flag()

iv = response [0:32]
print("iv = "  +iv)
ciphertext= response[32:]
print( "ciphertext = " + ciphertext)
flag= encrypt(ciphertext, iv)
flag=bytes.fromhex(flag)
print(flag)
