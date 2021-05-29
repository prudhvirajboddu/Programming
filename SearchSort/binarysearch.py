def bs(a,l,r,x):
    if r>=l: #right subarray length should be greater than left subarray
        mid=(l+r)//2 

        if a[mid]==x:
            return mid
        elif a[mid]>x: #if mid element is greater than x go for left array since x is smaller
            return bs(a,l,mid-1,x) 
        else:  # else go for right array
            return bs(a,mid+1,r,x)
    else:
        return -1
a=[2,4,5,6,10,15]
x=11
result = bs(a, 0, len(a)-1, x)
if result!=-1:
    print(result)
else:
    print(-1)
