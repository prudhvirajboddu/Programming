def getTotalX(a, b):
    maxA=max(a)
    minB=min(b)
    count=0
    for num in range(maxA,minB+1):
        left=all([num%numA==0 for numA in a])
        right=all([numA%num==0 for numA in b])
        count+=left*right
    return count

print(getTotalX([2,6],[24,36]))