def bubsort(arr):
    # arr.reverse()
    for _ in range(0,len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bubsort([1,2,3,4,5]))