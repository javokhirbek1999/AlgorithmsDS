"""
Time: O(n)
Space: O(n)
"""
def visitingAllCities(red: List[int], blue: List[int], blueCost: int) -> int:

    n = len(red)

    dp = [0]

    onBlueLine = False

    for i in range(n):

        takeRed = red[i]
        takeBlue = blue[i] + blueCost if not onBlueLine else blue[i]

        onBlueLine = True if takeBlue <= takeRed else False

        dp.append(dp[-1] + min(takeRed, takeBlue))

    return dp 


"""
Alternative

Time: O(n)
Space: O(n)
"""

def solve(red, blue, blueCost):
    ans=[0]
    r,b=0,blueCost 
    for i,j in zip(red,blue):
        r,b=min(r,b)+i,min(b,r+blueCost)+j
        ans+=[min(r,b)]  
    return ans 
