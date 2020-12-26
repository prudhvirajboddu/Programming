def rp():
    i=int(input())
    j=int(input())

    res=0

    while j>0:
        if (j&1): #bitwise and operation performed on binary numbers
            res+=i

        i=i<<1 #bitwise leftshift performed on binary numbers
        j=j>>1 #bitwise rightshift performed on binary numbers

    return res
print(rp())
