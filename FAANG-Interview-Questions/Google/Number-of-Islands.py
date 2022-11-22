"""
Time: O(N)
Space: O(MN * N)
"""

from typing import List


def numberOfIslands(grid: List[List[str]]) -> int:

    n = len(grid)
    m = len(grid[0])

    islands = 0
    
    for row in range(n):
        for col in range(m):
            if grid[row][col] == '1':
                visit(grid, row, col, n, m)
                islands += 1
    

    return islands


def visit(grid: List[List[int]], row: int, col: int, n: int, m: int) -> bool:

    if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] != '1':
        return
    
    grid[row][col] = '2'
    
    visit(grid, row+1, col, n, m)
    visit(grid, row-1, col, n, m)
    visit(grid, row, col+1, n, m)
    visit(grid, row, col-1, n, m)

