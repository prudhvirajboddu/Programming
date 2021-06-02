def difference(n,m):
    return abs(sum([i for i in range(1,m+1) if i%n!=0])-sum([i for i in range(1,m+1) if i%n==0]))

n,m=map(int,input().split())
print(difference(n,m))
