def minimumSwaps(arr):
    ref_arr = sorted(arr)
    index_dict = {v: i for i,v in enumerate(arr)}
    swaps = 0
    
    for i,v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]#assigning to unsorted array swap index
            arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix] #swapped array 
            index_dict[v] = to_swap_ix #reassigning the index array because of previous assignment
            # index_dict[correct_value] = i
            swaps += 1
            
    return swaps

print(minimumSwaps([4,3,1,2]))