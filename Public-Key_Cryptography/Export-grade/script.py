#! /usr/bin/env python3
import json
import pwn
import sympy


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


def main():
    remote = pwn.remote("socket.cryptohack.org", 13379)

    remote.recvuntil("Intercepted from Alice: ")
    intercepted_from_alice = json.loads(remote.recvline())
    intercepted_from_alice['supported'] = ["DH64"]
    remote.recvuntil("Send to Bob: ")
    remote.sendline(json.dumps(intercepted_from_alice))

    # We just forward Bobs request.
    remote.recvuntil("Intercepted from Bob: ")
    remote.sendline(remote.recvline())

    remote.recvuntil("Intercepted from Alice: ")
    resA = json.loads(remote.recvline())
    p=int(resA["p"],16)
    g=2
    A=int(resA["A"],16)
    remote.recvuntil("Intercepted from Bob: ")
    resB = json.loads(remote.recvline())
    B=int(resB["B"],16)
    remote.recvuntil("Intercepted from Alice: ")
    cipher=json.loads(remote.recvline())
    iv=cipher["iv"]
    ciphertext=cipher["encrypted_flag"]
    a=sympy.ntheory.residue_ntheory.discrete_log(p,A,g)

    shared_secret =  pow(B,a,p)
    flag = decrypt_flag(shared_secret, iv,ciphertext)
    pwn.log.info(flag)


if __name__ == "__main__":
    main()