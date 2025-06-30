def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1
    return -1 
arr = [1,4,5,6,9,10,13,15]
target = 9
result = binary_search(arr, target)

if result != -1:
   
    print(f"Element found at index {result}")
else:
    print("Element not found")
 
