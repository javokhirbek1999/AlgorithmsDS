def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def qucikSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        qucikSort(arr,low,pi-1)
        qucikSort(arr,pi+1,high)

# Time : O(nLogN)
# Space: O(n)

# When to use Quick Sort:
# 1. When average expected time is O(nLogN)

# When to avoid to use Quick Sort:
# 1. When space is a concern
# 2. When you nedd stable sort
