class Curve():

    def __init__(self, A, B, p):
        """
        Construcutor de clase que va a representar a la curva elíptica de la
        forma y^2 = x^3 + Ax + B (mod p).
        :param A: primer coeficiente de la curva.
        :param B: segundo coeficiente de la curva.
        :param p: el tamaño del campo sobre el cual se hace la curva.
        """
        self.a = A
        self.b = B
        self.p = p

    def is_on_curve(self, point):
        """
        Método de clase regresa true si un punto está en la curva, éste punto 
        está representado a manera de tupla, como (x, y).
        :param point: Una tupla de enteros representando a un punto.
        :return: true si el punto está en la curva, false en otro caso.
        """
        return ((point[1]**2 % self.p) == (((point[0]**3) + (self.a * point[0]) + self.b) % self.p))

    def determinant(self):
        """
        Regresa el determinante de una curva, recordando que su determinante
        es calculado de la forma 4A^3 + 27B^2.
        :return: El entero con el valor del determinante.
        """
        return ((4*(self.a ** 3)) + (27*(self.b **2))) #%self.p
#Auxiliar para modinv
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
#Saca el inverso de un numero a modulo m
def modinv(a, m):
    if a < 0:
        #print(a)
        a=cong(abs(a),m)
    #print(a)
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
#Auxiliar para pasar a positivo
def cong(n,m):
    k =1
    while k*m < n:
        k = k+1
    return ((k*m) - n) % m

def add_points(p, q, curve):
    """
    Dados un par de puntos y una curva elíptica, calcula el punto de la suma
    bajo la curva elíptica recibida como parámetro, se asume que p y q ya 
    forman parte de la curva.
    :param p: una tupla representando un punto de la curva.
    :param q: una tupla representando un punto de la curva.
    :param curve: una instancia de la clase de este script.
    :return: Una tupla que contiene el resultado de la suma o None en caso de
    que haya sido evaluada al punto infinito.
    """

    if(p==q):
        if p[1]==0 and 0 == q[1]:
            return None
        s1 = modinv((2*p[1])%curve.p, curve.p)
        s = ((3 * (p[0]**2)) + curve.a)*s1
    else:
        if p[0]==q[0]:
            return None
        s1 = modinv((q[0]-p[0]),curve.p)
        s = (q[1]-p[1])*s1
    x = (s**2) - p[0] - q[0]
    y = (s * (p[0]-x)) - p[1]
    return (x%curve.p,y%curve.p)


def scalar_multiplication(p, k, curve):
    """
    Dado un escalar del campo, k, calcula el punto kP bajo la definición
    de curvas elípticas.
    :param p: una tupla representando un punto de la curva.
    :param k: el escalar a multiplicar por el punto. 
    :param curve: la curva sobre la cual se calculan las operaciones.
    :return: una tupla representando a kP o None si al sumar ese punto cayó 
    en algún momento al punto infinito.
    """
    sum = p
    while k>1:
        #print (sum)
        if sum == None:
            sum = p
        else:
            sum = add_points(p,sum,curve)
        k = k-1
    return sum


#a = Curve(-7,10,19)
#p = (7,0)
#q = (2,7)
#print(a.is_on_curve((10,2)))
#print(a.determinant())
#print(scalar_multiplication(p,2,a))
#print(add_points(q,q,a))
