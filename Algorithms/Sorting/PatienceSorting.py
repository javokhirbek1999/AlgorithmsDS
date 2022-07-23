from typing import List


def patience_sort(arr: List[int]) -> List[int]:

    piles = []
    visited = {}

    for j in range(len(arr)):
        num = arr[j]
        if not piles:
            piles.append([num])
            visited[j] = True
        else:
            added = False
            for i in range(len(piles)):
                if piles[i][-1] >= num and i not in visited:
                    piles[i].append(num)
                    visited[i] = True
            if not added and j not in visited:
                piles.append([num])
                visited[j] = True
    
    res = []
    while piles:
        min_index = find_min(piles)
        res.append(piles[min_index].pop())
        if not piles[min_index]:
            piles.pop(min_index)

    return res

    
def find_min(arr):

    mn = arr[0][-1]
    index = 0

    for i in range(len(arr)):
        if arr[i][-1] <= mn:
            mn = arr[i][-1]
            index = i

    return index
