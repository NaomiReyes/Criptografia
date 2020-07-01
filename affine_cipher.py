from utils import CryptographyException
from utils import prime_relative

class Affine():

    def __init__(self, alphabet, A=None, B=None):
        self.alfabet = alphabet
        #Bloque de codigo a validar 
        if(A == None):
            self.A = 1
        else:
            self.A = A%len(self.alfabet)

        if not(self.sonCoprimos(self.A % len(self.alfabet))):
                raise CryptographyException#Llama la excepcion de usuario

        if(B == None):
            self.B = 0
        else:
            self.B = B

    def eucExt(self):
        r = [len(self.alfabet),self.A]
        s = [1,0] 
        t = [0,1]
        i = 1
        q = [[]]
        while (r[i] != 0): 
            q = q + [r[i-1] // r[i]]
            r = r + [r[i-1] % r[i]]
            s = s + [s[i-1] - q[i]*s[i]]
            t = t + [t[i-1] - q[i]*t[i]]
            i = i+1
        return ( t[i-1])

    def sonCoprimos(self, num1):
        if(num1 == 1):
            return True
        return not(len(self.alfabet)%num1 == 0)
            
    def lToN(self, letter):
        i = 0
        for e in self.alfabet:
            if(e == letter):
                return i
            i = i+1
        return -1
    
    def nToL(self, num, k,c,b):
        if(b == True):
            n = ((k + num)* c )% len(self.alfabet)	
        else:
            n = ((num*c) + k )% len(self.alfabet)
        return self.alfabet[n]
    
    def cipher(self, message):
        newMessage = ""
        for m in message:
            num = self.lToN(m)
            if( num != -1):
                newMessage = newMessage + self.nToL(num,self.B,self.A, False)
            else:
                print("Hay elementos que no pertenecen al alfabeto, por seguridad se detrendra el proceso :)")
                break
        return newMessage
        

    def decipher(self, criptotext):
        numero = len(self.alfabet) - self.B
        newMessage = ""
        for m in criptotext:
            num = self.lToN(m)
            if( num != -1):
                newMessage = newMessage + self.nToL(num,numero,self.eucExt(),True)
            else:
                break
        return newMessage

#p = Affine("HOLIM")
#print(p.cipher("HOLI"))
alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
message = "GOTVZÑOVÑZTLWGVTFTONJTWGNÑAIOIFDLGOIBÑSGLITNILWTLFGOIJTFÑNJIESGFRIBÑGXSXSTÑOJSWTVZIWGVIUVTOKTGOTUESVVGLITWTLZTTOESZÑTLINSOPVTNIAZTVZINILLGWIL"
a = Affine(alphabet, 10, 20)
#r = a.decipher(message)
#print (a.cipher(message))
print(a.decipher(message))
