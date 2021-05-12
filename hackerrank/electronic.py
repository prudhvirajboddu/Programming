from itertools import product
def returnres(key,boards,b):
    return max([i+j if i+j<=b else -1 for i,j in product(key,boards)])
print(returnres([50,40,20],[5,8,12],60))