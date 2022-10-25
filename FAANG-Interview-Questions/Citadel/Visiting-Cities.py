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
