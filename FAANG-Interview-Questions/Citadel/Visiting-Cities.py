"""
Time: O(n)
Space: O(n)
"""
def solve(red: List[int], blue: List[int], blueCost: int) -> int:

    n = len(red)

    dp = [0]

    prevBlueLine = -1

    for i in range(n):
        takeRed = dp[-1] + red[i]
        takeBlue = dp[-1] + blue[i] + blueCost if prevBlueLine != blue[i] else dp[-1] + blue[i]
        
        prevBlueLine = blue[i]
        
        curr = min(takeRed, takeBlue)

        dp.append(curr)
        

    return dp
