from prime_generator import generate_prime
from random import randint

class RSA():

    def __init__(self):
        """
        Constructor de RSA, aqui se deben de generar los primos p y q
        para que puedan ser vistos por toda la clase, asi como la llave
        publica y privada.
        """
        #Aqui tambien deben de generar su priv_key y pub_key
        self.p = generate_prime()
        self.q = generate_prime()
        self.n = (self.p) * (self.q)
        self.pub_key = self.calculaE()
        self.priv_key = self.modinv(self.pub_key,self.__phi__())
        self.escribePub()
        self.escribePriv()

    def __phi__(self):
        """
        Funcion completamente privada y auxiliar, unicamente para el uso de las
        pruebas unitarias.
        :return: el numero de primos relativos con n.
        """
        return (self.p - 1) * (self.q -1)

    def escribePub(self):
        f = open ('pub_key.pem','w')
        f.write('('+ str(self.n) + ' , '+ str(self.pub_key) + ')')
        f.close()

    def escribePriv(self):
        f = open ('priv_key.pem','w')
        f.write('('+ str(self.n) + ' , '+ str(self.priv_key) + ')')
        f.close()
        
    def mcd(self,a, b):
        resto = 0
        while(b > 0):
            resto = b
            b = a % b
            a = resto
        return a
    
    def calculaE(self):
        phi = self.__phi__()
        e = randint(2,phi)
        while (self.mcd(phi,e) != 1):
            e = randint(2,phi)
        return e

    def egcd(self,a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd((b % a), a)
            return (g, x - (b // a) * y, y)

    def modinv(self,a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m


    def fast_exp(self, n, a): #Calcula n^a mod m. 
    	m = self.n
        if(a == 1):
            return (n%m) 
        else: 
            h = self.fast_exp(n, a//2)
            r = (h*h) % m
            if a % 2 == 0:
                return r
            return (r*n) % m

    def encrypt(self, message):
        """
        Encripta un mensaje recibido como parametro y lo regresa a manera
        de lista de enteros.
        :param message: el mensaje a encriptar.
        :return: una lista de enteros con el mensaje encriptado.
        """
        l = []
        for m in message:
            c = self.fast_exp(ord(m), self.pub_key)
            l.append(c)
        return l
    
    def decrypt(self, criptotext):
        """
        Desencripta un criptotexto cifrado con RSA y lo regresa a manera
        de cadena, recuperando la informacion del mensaje original.
        :param criptotext: el mensaje recibido que se va a desencriptar.
        :return: una cadena con el mensaje original.
        """
        l = []
        for m in criptotext:
            c = self.fast_exp(m, self.priv_key)
            l.append(c)
        return l
    
mensaje = "Holi"
a = RSA()
#ver que son inversos
print((a.pub_key * a.priv_key)% a.__phi__())
enc = a.encrypt(mensaje)
print(enc)
print(a.decrypt(enc))
