k= 27
n = 7
e = True

while e:
    q = k // n
    r = k % n
    print(k," = ",n,"*",q,"+",r)
    if( r!= 0):
        k = n
        n = r
    else:
        e = False
        
def eucExt(a,b):
    r = [a,b]
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

print(eucExt(27,7))
