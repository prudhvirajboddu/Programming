n,m=5,1#map(int,input().split())
arr=[1,2,3,4,1]#list(map(int,input().split()))
c=0
if m not in arr:
        print(-1)
else:
        for i in range(n):
                if arr[i]==m:
                        c=i
        print(c)