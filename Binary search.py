def Binary_search(arr,target):
   for i in range(len(arr)):
       if arr[i] == target:
          return i
   return -1
arr = [1,4,5,6,9,10,13,15]
target = 9
result = Binary_search(arr,target) 
if result != -1:
    print(f"element found at index {result}")
else:
    print("element not found")
