def mergeSort(arr):

    if len(arr) <=1:
        return arr
    
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    L = mergeSort(L)
    R = mergeSort(R)

    i = j = 0
    merged = []

    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            merged.append(L[i])
            i += 1
        else:
            merged.append(R[j])
            j += 1

    merged.extend(L[i:])
    merged.extend(R[j:])
    
    return merged


array = [1, -1, 0, 3, 8, 2]
sorted_array = mergeSort(array)
print(sorted_array)
