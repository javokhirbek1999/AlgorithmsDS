# Time: O(n^2) -> Nested loops: one for looping through the array the min val and two for finding the min val
# Space: O(1) -> Sorts by swaping in-place without requiring additional space 
def selectionSort(arr):
    
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)): # Find min value index
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i] # Sort by swaping the values in-place: O(1)
    return arr

# When to use Selection Sort:
# 1. When space is the main concern
# 2. Easy to implement

# When to avoid to use Selection Sort:
# 1. When time is a concer 
