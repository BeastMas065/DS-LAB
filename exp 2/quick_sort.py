def partition(arr, low, high):
    pivot = arr[low]
    i, j = low, high

    while i<j:
        while arr[i] <= pivot and i<high:
            i += 1
        while arr[j] > pivot:
            j =+ 1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
             
    arr[low], arr[j] = arr[j], arr[low]

    return j


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


arr = list(map(int, input("Enter array(space separated): ").split()))

quick_sort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)
