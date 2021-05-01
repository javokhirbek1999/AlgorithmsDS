# Time: O(n^2) -> Bubble Sort uses nested loops
# Space: O(1) -> Bubble Sort sorts the data in-place
def bubbleSort(arr):
    
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# When to use Bubble Sort:
# 1. If the space is the main concern -> Space complexity: O(1) -> No extra space is required
# 2. Easy to implement

# When to avoid to use Bubble Sort:
# 1. If the time (speed) is the main concern -> Bubble Sort uses nested loop that costs O(n^2) time complexity
