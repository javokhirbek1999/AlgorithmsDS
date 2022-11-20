"""
n = # of houses
m = # of stores

Time: O(n * log(m))
Space: O(n)
"""

from typing import List

    
def solve(houses: List[int], stores: List[int]) -> List[int]:

    stores.sort()

    res = []

    for house in houses:
        closestStore = binarySearch(stores, house)
        res.append(closestStore)
    
    return res



def binarySearch(arr: List[int], target: int) -> int:

    low = 0
    high = len(arr)

    while low <= high:

        mid = low + (high - low) // 2
        
        if mid >= len(arr): return arr[-1]

        current = arr[mid]

        if current == target: 
            return target
        
        if current < target:
            low = mid + 1
        else:
            high = mid - 1
    
    
    lowDistance = abs(arr[low]-target)
    highDistance = abs(arr[high]-target)

    if lowDistance == highDistance:
        return min(arr[low], arr[high])
    
    if lowDistance < highDistance:
        return arr[low]
    
    return arr[high]
        
