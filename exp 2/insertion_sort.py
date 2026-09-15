def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f'iteration {i+1}: {arr}')
    return arr


arr = list(map(int, input("Enter array(space separated): ").split()))

print("Sorted array:", insertion_sort(arr))
