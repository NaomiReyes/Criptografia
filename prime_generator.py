from random import randint
from random import randrange
import sys

def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    """
    if(size == None or size < 100):
        size = randint(100, 151)
    range_start = 10**(size-1)
    range_end = (10**size)-1
    return randint(range_start, range_end)

def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    if n%2 == 0:
        return False
    s = n-1
    r = 0
    while s%2 == 0:
        r = r + 1
        s = s // 2
    for w in range(r-1):
        a = randrange(2,n-1)
        x = pow(a,s,n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = pow(x,2,n)
            if x == n-1:
                break
        else:
            return False
    return True


def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    z = int()
    total = 1
    i = 1
    
    while i < n:
        total *= i
        i +=1
    return (total+1)%n == z



