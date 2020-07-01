import random
from random import randint

class Participant():


    def __init__(self, p, g, participant):
        """
        Constructor de clase
        """
        self.P = p
        self.G = g
        self.participant = participant
        self.m = 0

        
    def seed(self):
        """
        Generador de la parte propia del intercambio de Diffie-Hellmann
        """
        if self.m == 0:
            self.m = random.randint(1, p-1)
        return (self.G ** self.m) % self.P

    def exchange(self):
        """
        Adquiero el número de la otra persona y calculo mi propia llave.
        """
        if self.m == 0:
            self.m = random.randint(1, p-1)
        return (self.participant.seed() ** (self.m)) % self.P
    

p, g = 103, 78
A, B = Participant(p, g, None), Participant(p, g, None)
A.participant = B
B.participant = A
keyA = A.exchange()
print(keyA)
print(B.exchange()==keyA)
