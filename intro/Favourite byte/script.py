from pwn import *
cipher="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
c=bytes.fromhex(cipher)

for i in range(0,255):
    plain=xor(c,i)
    try:
        if ("crypto" in plain.decode("utf-8")):
            print(plain.decode("utf-8"))
    except :
        continue
