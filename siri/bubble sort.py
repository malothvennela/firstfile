def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                return arr
            arr = [64,34,25,12,22,11,90]
            print("original array:",arr)
              sorted_arr = bubble_sort(arr)
            print("sorted array:",sorted_arr)

