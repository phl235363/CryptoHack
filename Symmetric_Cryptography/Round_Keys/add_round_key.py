from Cryptodome.Util.number import *
from  pwn import xor
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]



def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    result=b""
    for lists in  matrix:
        for item in lists :
            result+=(long_to_bytes(item))
    
    return result



def add_round_key(s, k):
    result=[]
    for i in range (0,4):
        tmp=[]
        for j in range (0,4):
            tmp.append(s[i][j]^k[i][j])
        result.append(tmp)
    
    return result
a=add_round_key(state,round_key)




print(matrix2bytes(a))

