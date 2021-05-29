def cups(N,L,x):
    if sum(x)<L:
        return -1
    else:
        return L//N

print(cups(6,15,[3,3,4,1,5,5]))