import time

def recursive_factorial(n):
    if (n>0):
        return n*recursive_factorial(n-1)
    return 1

def iterative_factorial(n):
    if (n>0):
        total = 1
        while(n>1):
            total*=n
            n-=1
        return total
    return 1

def time_iterative(n):
    tiempos = []
    enes = []
    for i in range(1,n+1):
        i*=100
        t1 = time.time()*1000
        iterative_factorial(i)
        t2 = time.time()*1000
        enes.append(i)
        tiempos.append(t2-t1)
    return enes,tiempos

def time_recursive(n):
    tiempos = []
    enes = []
    for i in range(1,n+1):
        i*=100
        t1 = time.time()*1000
        recursive_factorial(i)
        t2 = time.time()*1000
        enes.append(i)
        tiempos.append(t2-t1)
    return enes,tiempos
