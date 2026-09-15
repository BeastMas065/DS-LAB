def LinearSearch(n, arr, key):
    for i in range(len(arr)):
        if key == arr[i]:
            return i
    return -1

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter array(space separated): ").split()))
key = int(input("Enter number to find: "))
result = LinearSearch(n, arr, key)
if result == -1: print("Key not found")
else: print(f'key found at position : {result+1}')