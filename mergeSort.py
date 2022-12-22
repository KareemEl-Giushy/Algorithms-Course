def merge(arr, left, right):
    i = j = k = 0

    while i < len(right) and j <  len(left):
        if right[i] < left[j]:
            arr[k] = right[i]
            i += 1
        else:
            arr[k] = left[j]
            j += 1
        k += 1

    while i < len(right):
        arr[k] = right[i]
        i += 1
        k += 1

    while j < len(left):
        arr[k] = left[j]
        j += 1
        k += 1

def mergeSort(arr : list):
    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        merge(arr, left, right)




arr = [4, 2, 1, 3, 7, 5]
mergeSort(arr)
print(arr)