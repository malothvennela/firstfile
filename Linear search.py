def linear_search(arr,target):
   for i in range(len(arr)):
       if arr[i] == target:
          return i
   return -1
arr = [2,4,5,12,16,20,22]
target = 20
result = linear_search(arr,target) 
if result != -1:
    print(f"element found at index {result}")
else:
    print("element not found")

