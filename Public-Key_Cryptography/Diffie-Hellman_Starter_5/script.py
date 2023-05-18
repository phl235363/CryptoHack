import json
resa={"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0x4b9b01c258eb9d924069ee0b0a7b38b78a20429aa5996402e0f5a04d72834e194393a85d84261158f22e5fb01eb080041cec57f05343ce10315da6281419dab3ceeb7463adf9e37ff0fc3689e66be9807b43510670f453b4f8a5cbf93dd542cedcce1fea30934e937b8f1af15267ca31e1067237a22a5d72934a607cf4ecb41a3f36f399a1466aa0f9367cee122248ac56b417c6b34da079a74005d1e7c8ca33c528f753c18fa68cc71a6fd460fcf13efaaf9092e7ac250d3e749a643e25c51"}

myp=int (resa["p"],16)
myg=int(resa["g"],16)
myKey=63
myA=pow(myg,myKey,myp)
repB={}
repB["p"]=hex(myp)
repB["g"]=hex(myg)
repB["A"]=hex(myA)


A=int(resa["A"],16)
key=pow(A,myKey,myp)
print(key)
