class Caesar():

    def __init__(self, alphabet, key=None):
        """
        Constructor de clase que tiene como parámetro todos los atributos
        que necesita el algoritmo de cifrado de César.
        Parámetro:
            alphabet -- el alfabeto sobre quien se cifra el mensaje.
            key -- el tamaño del desplazamiento sobre el alfabeto, si es
                   None, se debe de escoger una llave aleatoria, válida.
        """
        self.alphabet = alphabet
        if(key == None):
            self.key = 0
        else:
            self.key = key 

    def lToN(self, letter):
        i = 0
        for e in self.alphabet:
            if(e == letter):
                return i
            i = i+1
        return -1
    
    def nToL(self, num, k):
        n = (num + k) % len(self.alphabet)
        return self.alphabet[n]
    
    def cipher(self, message, flag=None):
        """
        Cifra el mensaje recibido como parámetro con el algoritmo de
        cifrado césar, un desplazamiento sobre el alfabeto predefinido.
        Parámetro:
            message -- el mensaje a cifrar.
        """
        if(flag == None):
            flag = False
            
        newMessage = ""
        for m in message:
            num = self.lToN(m)
            if (num == -1 and m == " "):
              if flag:
                  newMessage = newMessage + m
            elif( num != -1):
                newMessage = newMessage + self.nToL(num, self.key)
            else:
                print("Hay elementos que no pertenecen al alfabeto, por seguridad se detrendra el proceso :)")
                break
        return newMessage

    def decipher(self, criptotext, flag=None):
        """
        Descifra el mensaje recuperando el texto plano siempre y cuando
        haya sido cifrado con el algoritmo de césar.
        Parámetro:
            cryptotext -- el mensaje a descifrar.
        """
        if(flag == None):
            flag = False
            
        newMessage = ""
        for m in criptotext:
            num = self.lToN(m)
            if (num == -1 and m == " "):
              if flag:
                  newMessage = newMessage + m
            elif( num != -1):
                newMessage = newMessage + self.nToL(num,len(self.alphabet)-self.key)
            else:
                print("Hay elementos que no pertenecen al alfabeto, por seguridad se detrendra el proceso :)")
                break
        return newMessage
    

