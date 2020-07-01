import EllipticCurves
import random
import math
from EllipticCurves import *

class ECIES():
    def __init__(self, curve, A, B, N, s, p):
        self.curve = curve
        self.A = A
        self.B = B
        self.N = N
        self.s = s
        self.p = p

    
    def encrypt(self, message):
        alphabet=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcde"
        lista = []
        for e in message:
            p = ord(e)
            k = random.randrange(1,self.N)
            kA=EllipticCurves.scalar_multiplication(self.A,k,self.curve)
            kB=EllipticCurves.scalar_multiplication(self.B,k,self.curve)
            pc = self.cPC(kA)
            lista.append((pc,((alphabet.index(e)* kB[0])%self.p)))
        return lista


    def decrypt(self, criptotext):
        alphabet=" ABCDEFGHIJKLMNOPQRSTUVWXYZabcde"
        res = ""
        for e in criptotext:
            e1, e2 = e
            x = self.point_decompress((e1[0]),(e1[1]))
            f = EllipticCurves.scalar_multiplication((e1[0],x),self.s,self.curve)
            m = ( e2 * modinv(f[0],self.p)) % self.p
            res += str(alphabet[m])
        return res

    def cPC(self,p):
        return (p[0],p[1]%2)
    
    def point_decompress(self,x,i):
        z = (pow(x,3) + self.curve.a*x + self.curve.b)% self.curve.p 
        while True:
            raiz = math.sqrt(z)
            n = int(raiz)
            if (n*n == z):
                break
            else:
                z += self.p
        if i==0:
            raiz = raiz * -1
        return int(raiz)



c = Curve(7, 19, 31)
p = 31
A = (18, 26)
B = (10, 2)
cipher = ECIES(c, A, B, 39, 8, 31)
result = cipher.encrypt("PUMAS")
desresult = cipher.decrypt(result)
print(result)
print(desresult)
