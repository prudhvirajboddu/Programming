def fibonacci(n):
    fib={}
    fib[0]=fib[1]=1
    for i in range(2,n):
        fib[i]=fib[i-1]+fib[n-2]
    return fib 
print(fibonacci(10))