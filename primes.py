import math

def print_factors(x):
   for i in range(1, x + 1):
       if x % i == 0 and i>1:
           return i

def primes(n):

    if n>2:
        for i in range(2,n):
            if n%i==0:
                # print(n,"is not prime")
                return print_factors(n)
        else:
            return 1
    else:
        return 1


print(primes(175))