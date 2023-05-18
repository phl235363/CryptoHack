import hashlib
import random
from Crypto.Cipher import AES

# /usr/share/dict/words from




# @chal.route('/passwords_as_keys/decrypt/<ciphertext>/<password_hash>/')
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


# @chal.route('/passwords_as_keys/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}

# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words


# result = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
cipher="c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"


with open('words','r')as f:
    for word in f:
        word=word.strip()
        attempted_key=hashlib.md5(word.encode()).hexdigest()
        plain=decrypt(ciphertext=cipher,password_hash=attempted_key)

        plaintext=bytes.fromhex(plain['plaintext'])
        try:
            plaintext=plaintext.decode('utf-8')
            if 'crypto' in plaintext:
                print(plaintext)
                print(word)
        except:
            continue
            