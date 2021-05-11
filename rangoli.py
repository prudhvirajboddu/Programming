def print_rangoli(size):
    import string
    al=string.ascii_lowercase
    L=[]
    for i in range(size):
        s="-".join(al[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3,'-'))
    p=L[::-1]+L[1:]
    print(*(p),sep="\n")
