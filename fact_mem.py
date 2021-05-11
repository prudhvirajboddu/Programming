import time
s=time.time()
def naive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*naive(n-1)
def fact(n):
    lookup={}
    if n in lookup:
        return lookup[n]
    elif n==0 or n==1:
        return 1
        lookup[n]=1
    else:
        f=n*fact(n-1)
        lookup[n]=f
    return f
print(fact(100),time.time()-s,sep="\n") 