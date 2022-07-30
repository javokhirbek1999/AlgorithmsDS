"""
Bubble Sort Algorithm using Backtracking

Time: O(n^2)
Space: O(n)
"""

from typing import List

def bubbleSort(arr: List[int], n: int) -> None:

    if n == 1:
        return 
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        
    bubbleSort(arr, n-1)
