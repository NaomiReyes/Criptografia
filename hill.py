import math 
import numpy as np
import random
from utils import CryptographyException
class Hill():

    def __init__(self, alphabet, n, key=None):
        self.alphabet = alphabet
        self.key = key 
        self.n = n
        #matriz de la llave
        self.keyGenerated = []
        #inicializa la matriz de arriba
        if(self.key == None):
            self.keyGenerated = np.array(self.identidad(int(math.sqrt(n))))
        else:
            self.generateMatrixKey(n,self.key)
            
        if self.det(self.keyGenerated) == 0:
            raise CryptographyException
        self.Matrixlength = int(math.sqrt(n))

    def identidad(self,n):
        idn = []
        for i in range(n):
            idn.append([])
            for j in range(n):
                if j==i:
                    idn[i].append(1)
                else:
                    idn[i].append(0)
        return idn


    #Genera la matriz cuadrada dada la llave 
    def generateMatrixKey(self, length, key):
        n = int(math.sqrt(length)) #tamaño de la matriz cuadrada.
        i = 0
        a= []
        while i < n:
            row = []
            for s in key[i*n:(i+1)*n]:
                row.append(self.lToN(s))
            a.insert(i, row)
            i +=1

        self.Matrixlength = n
        self.keyGenerated = np.array(a)

    #Genera la matriz de n*1 del mensaje
    def genetareMatrixMessage(self, subMesage):
        n = self.Matrixlength
        i = n
        subMatrix = []
        row = []
        for s in subMesage:
            subMatrix.insert(i, [self.lToN(s)])
        i -=1

        return np.array(subMatrix)


    def lToN(self, letter):
        return self.alphabet.index(letter)

    #Funcion que rellena los caracteres faltantes
    def fill(self, message):
        differentLen = len(message)% self.Matrixlength
        while differentLen > 0: 
            message += self.alphabet[0]
            differentLen -=1
        return message


    def cipher(self, message):
        message = self.fill(message.replace(' ', ''))
        n = self.Matrixlength
        i = 0
        ciphered = "";
        while i < len(message)/n:
            subMessage = self.genetareMatrixMessage(message[i*n:(i+1)*n]) #generamos la matriz 1xn del mensaje
            i +=1
            #iteramos sobre la multiplicacion de las matrices
            for x in np.nditer(self.keyGenerated.dot(subMessage)): 
                ciphered += self.alphabet[x%len(self.alphabet)]

        return ciphered
     

    def quita (self,fila, columna, m):
        newM = []
        ni=0
        mj=0
        for i in range(len(m)):
            if i != fila:
                newM.append([])
                for j in range(len(m[i])):
                    if(j != columna):
                        elem = m[i][j]
                        newM[ni].append(elem)
                        mj = mj+1
                ni = ni+1
        return newM

    def det2 (self,m):
        return ((m[0][0]*m[1][1]) - (m[0][1]*m[1][0])) % len(self.alphabet)
    
    #Saca el determinante de una matriz
    def det(self,m):
        determinante = 0
        p =0
        if len(m) == 1:
            return m[0][0]
        if len(m) == 2:
            return self.det2(m)
        else:
            for i in range(len(m)):
                p = (m[0][i]*((-1)**(0+i))*(self.det(self.quita(0,i,m))))
                determinante = determinante + p
            return determinante % len(self.alphabet)
        
     #Sacar la matriz adyacente   
    def adjMatr (self,m):
        n = len(m)
        adj = []
        for i in range(n):
            adj.append([])
            for j in range(n):
                adj[i].append(((-1)**(i+j)) * (self.det(self.quita(i,j,m))))
        return adj
    
    #sacar el inverso multiplicativo del determinante
    def eucExt(self):
        r = [len(self.alphabet),self.det(self.keyGenerated)]
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
    

    
    def decipher(self, ciphered):
        ciphered = self.fill(ciphered.replace(' ', ''))
        adj = np.array(self.adjMatr(self.keyGenerated))
        trans = adj.transpose()
        inv = self.eucExt()
        matrizInversa= trans*inv
        n = self.Matrixlength
        i = 0
        desciphered = "";
        while i < len(ciphered)/n:
            subMessage = self.genetareMatrixMessage(ciphered[i*n:(i+1)*n]) #generamos la matriz 1xn del mensaje
            i +=1
            #iteramos sobre la multiplicacion de las matrices
            for x in np.nditer(matrizInversa.dot(subMessage)):
                desciphered += self.alphabet[x%len(self.alphabet)]
                
        return desciphered

