"""
Time: O(n ^ 2)
Space: O(n)
"""
def triplets(arr: List[int], t: int) -> int:

    n = len(arr)

    arr.sort()

    c = 0

    for i in range(n-2):
        
        left = i + 1
        right = n-1


        while left < right:

            _sum = arr[i] + arr[left] + arr[right] 
            
            if _sum <= t:
                c += 1
                right -= 1
            else:
                left += 1
    
    return c
