def twoSum(A,t):
    prevsum={}
    for i,n in enumerate(A):
        p=t-n
        if p in prevsum:
            return [prevsum[p],i]
        prevsum[n]=i
    return