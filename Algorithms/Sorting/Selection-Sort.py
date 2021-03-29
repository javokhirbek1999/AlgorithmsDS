# Time: O(n) 
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)): # <- O(n)
        if arr[i]<smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)): # <-- O(n)
        smallest = find_smallest(arr) # <-- O(n)
        new_arr.append(arr.pop(smallest))
    return new_arr
# Time: O(n x n) = O(n^2)

# Selection sort costs O(n^2) as it has two nested loops: 
# 1. First loop for finding the smallest number in the array
# 2. For looping through the array to append the elements in order from smallest to greatest