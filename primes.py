n=int(input())
i2=i3=i5=0
primes=[1]
for i in range(1,n):
    primes[i]=min(2*primes[i2],5*primes[i3],5*primes[i5])
    primes.append(primes[i])
    
    i2+=1
    i2+=1
    i3+=1
print(primes[n])