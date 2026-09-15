def binary_search(n, arr, key):
    low = 0
    high = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array(space separated): ").split()))
key = int(input("Enter key to find: "))

result = binary_search(n, arr, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
