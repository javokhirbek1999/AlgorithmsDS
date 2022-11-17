"""
k = n + m
Time: O(k log k)
Space: O(k)
"""
from typing import List

def solve(S: List[int], E: List[int]) -> int:

    # 1 for come, 2nd for leave
    guestAttendance = [(s, 1) for s in S] + [(e, -1) for e in E]

    guestAttendance.sort()

    chairs = 0
    freeChairs = 0
    maxChairs = 0

    
    for _, status in guestAttendance:

        if status == 1:
            # if not free chairs, bring new one
            if freeChairs == 0:
                chairs += 1
            else:
                # if free chairs are available, then use them
                freeChairs -= 1
        else:
            chairs -= 1
            freeChairs += 1
        
        maxChairs = max(maxChairs, chairs)
    
    return maxChairs
