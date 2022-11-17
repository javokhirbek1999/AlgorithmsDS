"""
n = len(text)

Time: O(n)
Space: O(1)

keyboard len is always 26 but characters are in different order
"""

def solve(keyboard: str, text: str) -> int:

    alpha = {keyboard[i]:i for i in range(len(keyboard))}

    currentIndex = 0

    totalTime = 0

    for char in text:
        totalTime += abs(alpha[char]-currentIndex)
        currentIndex = alpha[char]

    return totalTime


print(solve("abcdefghijklmnopqrstuvwxy", "dude"))
