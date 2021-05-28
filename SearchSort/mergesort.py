def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        # assigning mid
        L = arr[:mid]
        # assigning left sub array
        R = arr[mid:]
        # assigining right array

        mergesort(L)
        # recursive left subarray

        mergesort(R)
        # recursive right subarray

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:  # comparing sub array elements ith and jth index
                arr[k] = L[i]
                # moving left sub array ith element to arr[k]
                # still element arr[k] is present in right subarray
                i += 1
            else:
                arr[k] = R[j]
                # moving right sub array jth element to arr[k]
                # still element arr[k] is present in left subarray
                j += 1
            k += 1
            # incrementing kth posistion irrespective of comparison b/w l[i] and r[i]

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

arr = [12, 5, 13, 11, 6, 7]
print(mergesort(arr))
