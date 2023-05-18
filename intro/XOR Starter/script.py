a="label"
b=""
for c in a :
    num= ord(c)
    print(c)
    print(num)
    num=num^13
    print(num)
    print(chr(num))
    b+=chr(num)
print(b)
