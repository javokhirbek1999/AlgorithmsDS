"""
Time: O(n^3*m)
Space: O(n^2)

Variation: N-Queens
"""

from typing import List


def solve(n: int) -> List[List[int]]:
    
    occupied = []
    matrix = []

    for _ in range((n*n)+1):
        occupied.append(False)

    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(-1)
        matrix.append(row)

    if backtrack(matrix, 0, 0, n, occupied):
        return matrix
    


def backtrack(matrix: List[List[int]], row: int, col: int, n: int, occupied: List[List[int]]) -> bool:

    if col == len(matrix[0]):
        row += 1
        col = 0
    
    if row == n:
        return isOK(matrix, n)
    

    for i in range(1,(n*n)+1):
        if not occupied[i]:
            occupied[i] = True
            matrix[row][col] = i
            if backtrack(matrix, row, col+1, n, occupied):
                return True
            occupied[i] = False
            matrix[row][col] = -1
    
    return False



def isOK(matrix: List[List[int]], n: int):
    
    current = sum(matrix[0])
    # Check rows
    for row in matrix:
        if sum(row) != current:
            return False
    

    # Check cols
    for c in range(len(matrix[0])):
        curr = 0
        for r in range(n):
            curr += matrix[r][c]
        
        if curr != current:
            return False


    diagRight = 0
    col = 0
    # Check Diagonal Right
    for row in range(n):
        diagRight += matrix[row][col]
        col += 1
    
    if diagRight != current:
        return False
    

    diagLeft = 0
    col = n-1
    # Check Diagoanl Left
    for row in range(n):
        diagLeft += matrix[row][col]
        col -= 1
    
    if diagLeft != current:
        return False
    
    return True

        

for row in solve(3):
    print(row)
