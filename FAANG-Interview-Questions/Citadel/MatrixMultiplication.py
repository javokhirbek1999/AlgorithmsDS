"""
O(n * m)
Space: O(1)
"""

from typing import List


def matrixMultiplication(matrix: List[List[int]]) -> List[int]:


    n = len(matrix)
    m = len(matrix[0])


    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):

            up = 0 if i == 0 else matrix[i-1][j]
            left = 0 if j == 0 else matrix[i][j-1]
            topLeft = 0 if i == 0 or j == 0 else matrix[i-1][j-1]

            matrix[i][j] -= up + left - topLeft
    

    return matrix

