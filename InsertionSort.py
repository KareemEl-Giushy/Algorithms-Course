def insertionSort(arr : list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [4, 1, 2, 5, 3 ,7]

insertionSort(arr)

print(arr)
        