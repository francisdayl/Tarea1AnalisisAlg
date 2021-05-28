from time import time

l_numers = ["1","2","5","8","10","12","15","20","25","30","35","40"]

def iterative_fibonacci(n):
    a, b = 0,1
    L=[]
    while len(L) < n:
        a, b = b, a+b
        L.append(a)
    return L

def recursive_fibonacci(n=1,L=[]):
    if n <= 1:
       return n,[n]
    else:
        fibo,lt= recursive_fibonacci(n-1,L) 
        fibo2= recursive_fibonacci(n-2,L)[0]
        lt.append(fibo2+fibo)
        return fibo+fibo2,lt

def recursive_fibonacci2(n):
    if n <= 1:
       return n#,[n]
    else:
        return recursive_fibonacci2(n-2)+recursive_fibonacci2(n-1) 

def time_iterative(n):
    tiempos = []
    enes = []
    for pos in range(1,l_numers.index(str(n))+1):
        i = int(l_numers[pos])
        enes.append(i)
        t1=time()
        iterative_fibonacci(i)
        tiempos.append(round(time()-t1,2))
    return enes,tiempos

def time_recursive(n):
    tiempos = []
    enes = []
    for pos in range(1,l_numers.index(str(n))+1):
        i = int(l_numers[pos])
        t1=time()
        recursive_fibonacci2(i)
        tiempos.append(round(time()-t1,2))
        enes.append(i)
    return enes,tiempos
