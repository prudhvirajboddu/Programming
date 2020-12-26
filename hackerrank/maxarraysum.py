def maxarraysum(arr):
    if len(arr)==0:
        return 0
    arr[0]=max(0,arr[0])
    if len(arr)==1:
        return arr[0]
    arr[1]=max(arr[0],arr[1])
    """
     Initial and second elements are computed manually 
     next max of previous and present+element beside the previous are computed 
     Thus the non-adjacent elements subset sum is computed
     [1,2,3,4,5,6] ans=12
     0  1  2 3 4 5  len=6
     arr[0]=1
     arr[1]=2
     arr[2]=max(2,3+1)=4
     arr[3]=max(4,4+2)=6
     arr[4]=max(6,5+4)=9
     arr[5]=max(9,6+6)=12 
     return 12 as it is maximum of non-adjacent elements sum
    """
    for i in range(2,len(arr)): 
        arr[i]=max(arr[i-1],arr[i]+arr[i-2])
    return arr[len(arr)-1]

print(maxarraysum([1,2,3,4,5,6]))