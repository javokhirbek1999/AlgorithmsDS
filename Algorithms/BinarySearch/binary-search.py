# O(log(n))
def binary_search(arr,item):
    low = arr[0]
    high = arr[-1]

    while low<=high:
        mid = (low+high)//2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > arr[mid]:
            low = mid+1
        else:
            high = mid-1
        return -1    
