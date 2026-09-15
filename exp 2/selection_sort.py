def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f'iteration {i+1}: {arr}')
    return arr


arr = list(map(int, input("Enter array(space separated): ").split()))

print("Sorted array:", selection_sort(arr))
