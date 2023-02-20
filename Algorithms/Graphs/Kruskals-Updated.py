"""
Time: O(E log E + E log V)
Space: O(E)
"""

from collections import namedtuple

class Node:

    def __init__(self, parent: int, rank: int) -> None:
        self.parent = parent
        self.rank = rank

mst = set()

def printMST(mst: set):

    print("MST: ")
    for p in mst:
        print(f"{p.src} -> {p.dest} | {p.weight}")


def find(point, dsuf):
    
    if dsuf[point].parent == -1:
        return point
    
    dsuf[point].parent = find(dsuf[point].parent, dsuf)

    return dsuf[point].parent

def union(fromP, toP, dsuf):

    if dsuf[fromP].rank > dsuf[toP].rank:
        dsuf[toP].parent = fromP
    elif dsuf[fromP].rank < dsuf[toP].rank:
        dsuf[fromP].parent = toP
    else:
        dsuf[fromP].parent = toP
        dsuf[toP].rank += 1


def kruskals(edgeList: list, V: int, E: int, dsuf) -> None:

    edgeList.sort(key=lambda x:x.weight)

    i, j = 0, 0

    while i < V-1 and j < E:

        fromP = find(edgeList[j].src, dsuf)
        toP = find(edgeList[j].dest, dsuf)
        
        if fromP == toP:
            j += 1
            continue

        union(fromP, toP, dsuf)
        mst.add(edgeList[j])
        i += 1


def main():
    
    E, V = 10, 6

    dsuf = [Node(-1, 0) for _ in range(V)]
    
    edgeList = [namedtuple('Edge', 'src dest weight') for _ in range(E)]

    for i in range(E):
        
        source, dest, weight = list(map(int, input().split()))

        edgeList[i].src = source
        edgeList[i].dest = dest
        edgeList[i].weight = weight
    
    kruskals(edgeList, V, E, dsuf)
    printMST(mst)


if __name__ == "__main__":
    main()
