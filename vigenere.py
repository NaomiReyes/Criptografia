from caesar_cipher import Caesar

class Vigenere():

    def __init__(self, alphabet, password=None):
        #Recomendación, ingeniárselas para no cargar siempre O(n^2) en memoria aunque esto no
        #será evaluado, con n el tamaño del alfabeto.
        """
        Constructor de clase, recibe un parámetro obligatorio correspondiente al alfabeto
        y un parámetro opcional que es la palabra clave, en caso de ser None, entonces
        generar una palabra pseudoaleatoria de al menos tamaño 4.
        :param alphabet: Alfabeto a trabajar con el cifrado.
        :param password: El password que puede ser o no dada por el usuario.
        """
        self.alphabet = alphabet
        if password == None:
            self.password = "Holi"
        else:
            self.password = password
        self.cesar = Caesar(self.alphabet)

    
        
    def lToN(self, letter):
        i = 0
        for e in self.alphabet:
            if(e == letter):
                return i
            i = i+1
        return -1
    
    def convierteLlave(self,llave):
        llaveInt = []
        for i in llave:
            llaveInt.append(self.lToN(i))
        return llaveInt
            
    def cipher(self, message):
        """
        Usando el algoritmo de cifrado de vigenere, cifrar el mensaje recibido como parámetro,
        usando la tabla descrita en el PDF.
        :param message: El mensaje a cifrar.
        :return: Una cadena de texto con el mensaje cifrado.
        """
        j = 0
        llave = self.convierteLlave(self.password)
        longitud = len(llave)
        strg = ""
        for i in message:
            self.cesar.key = llave[j%longitud]
            strg = strg+(self.cesar.cipher(i))
            j = j+1
        return strg

    def decipher(self, ciphered):
        """
        Implementación del algoritmo de decifrado, según el criptosistema de vigenere.
        :param ciphered: El criptotexto a decifrar.
        :return: El texto plano correspondiente del parámetro recibido.
        """
        j = 0
        llave = self.convierteLlave(self.password)
        longitud = len(llave)
        strg = ""
        for i in ciphered:
            self.cesar.key = llave[j%longitud]
            strg = strg+(self.cesar.decipher(i))
            j = j+1
        return strg


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = "SZHDYIAGJOKXGEQEBOSDMCBAEOECYAYQMSRVUNGEESJRAURDWXFRHGEALOTXHSGAFHVJXOEOSELRYNZISAFAGAYTJOKJGAYTJOKXUQHIWBDRUMBRTIJLUCBNKHRWNENLIIVCLAGOVSRVIRUADZFMCAZAFHVHMOLDAODJHTRADELNXENMGFDNNRNTSHIRONSAFHVZOIRRGJVAULDUWAVVUTNYEOKXULDUWAVZOIRRWJVANRVUFTRWNEFISSJCYPNGGDRMYCRMARVBYOFUJIVPIANQMSCVCPHNVCEXLEAOBCUNYNGRSASXMMBDGGZWZEYIRAVEYOCEJCPXJOEMWXFAJAETARFNMCBJGRVZOIRNFCHDCEEOKSIECOYEFHFNGPYEGELNXEDUASEWIMRQMWVAYVVLVSJYIJBJMOEJLAZIJSQMYAFBSXV"
#short = "SOCD"
#for j in message:
short = "SORJUANA"
#print(j)
vig_short = Vigenere(alphabet, short)
ciphered = vig_short.decipher(message)
#print(ciphered +" == TSMWTSNFBEFLPJWUENG")
print(ciphered)

#vig_short = Vigenere(alphabet, short)
#ciphered = vig_short.decipher(message)
#print(ciphered)

