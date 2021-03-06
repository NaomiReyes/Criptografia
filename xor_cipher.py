def cipher(message):

    """
    Cifra el mensaje recibido como parámetro con el algoritmo de cifrado
    XOR.
    Parámetro:
       message -- el mensaje a cifrar.
    """
    newString = ""
    for i in message:
        newString = newString + chr((ord(i) ^ 1) % 225); 
      
    return newString; 

def decipher(criptotext):
    """
    Descifra el mensaje recuperando el texto plano siempre y cuando haya
    sido cifrado con XOR.
    Parámetro:
       cryptotext -- el mensaje a descifrar.
    """
    newMessage = ""
    for i in criptotext: 
        newMessage = newMessage + chr((ord(i) ^ 1) % 225)
        
    return newMessage

m = cipher("Ésta es una frase en español")
print(m)
print(decipher(m))
