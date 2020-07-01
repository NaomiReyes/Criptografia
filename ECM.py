import EllipticCurves
from random import randint

def lenstra(n):
    """
    Implementación del algoritmo de Lenstra para encontrar los factores
    primos de un número n de la forma n = p*q. Se asume que la proposición
    anterior es cierta, es decir, que en efecto n = p*q, regresando ambos
    factores de n.
    """
    e = encuentra(n)
    fac = aux(e[0],e[1],e[2])
    while((fac[1]==n) or (fac[0]==n) or (fac[1]==1) or (fac[0]==1)):
        e = encuentra(n)
        fac = aux(e[0],e[1],e[2])
    return fac

def aux(x,y,c):
    p1 = (x,y)
    p2 = (x,y)
    dx = 2*y
    n=c.p
    while mcd(dx,n)==1:
        #print("okas")
        p3 = EllipticCurves.add_points(p1,p2,c)
        p1 = p2
        p2 = p3
        if p1 == p2:
            dx = 2*p1[1]
        else:
            dx = p2[0]-p1[0]
    factor = mcd(dx,n)
    return (factor, int(n/factor))

def saca_random(n):
    x = randint(0,n-1)
    y = randint(0,n-1)
    a = randint(0,n-1)
    b = (x**3)-(y**2)+(a*x)
    c = EllipticCurves.Curve(a,b,n)
    return (x,y,c)

def encuentra(n):
    var = saca_random(n)
    while mcd(var[2].determinant(),n)!=1:
        var = saca_random(n)
    return var

def mcd (a,b):
    resto = 0
    while(b>0):
        resto=b
        b=a%b
        a=resto
    return a

#e = encuentra(12366)
#print(lenstra(130063))
 
