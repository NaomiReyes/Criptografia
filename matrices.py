def menToVec(m,n):
    vectores = []
    tam = len(m)
    res = tam//n
    mod = tam %n
    k =0
    if mod==0:
        r =0
    else:
        r=1
    for i in range(res+r):
        vectores.append([])
        for j in range(n):
            if k <= (tam-1):
                vectores[i].append(m[k])
            else:
                vectores[i].append(-1)
            k = k+1
    return vectores
            
            
def strToMtr (string,n):
    matriz = []
    e = 0
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(string[e])
            e = e+1
    return matriz
        
def quita (fila, columna, m):
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

def det2 (m):
    return (m[0][0]*m[1][1]) - (m[0][1]*m[1][0])

def det(m):
    determinante = 0
    p =0
    if len(m) == 2:
        return det2(m)
    else:
        for i in range(len(m)):
            p = (m[0][i]*((-1)**(0+i))*(det(quita(0,i,m))))
            determinante = determinante + p
        return determinante % len(alphabet)

def identidad(n):
    idn = []
    for i in range(n):
        idn.append([])
        for j in range(n):
            if j==i:
                idn[i].append(1)
            else:
                idn[i].append(0)
    return idn

def adjMatr (m):
    n = len(m)
    adj = []
    for i in range(n):
        adj.append([])
        for j in range(n):
            adj[i].append(((-1)**(i+j)) * (det(quita(i,j,m))))
    return adj
a = [[1,2,3],[4,5,6],[7,8,9]]
#print(det(a))
#print(a)
#st = "Holiwistr"
#print(len(st))
#print(menToVec(st,3))
#print(identidad(4))
#print(strToMtr(st,3))
print(adjMatr(a))
