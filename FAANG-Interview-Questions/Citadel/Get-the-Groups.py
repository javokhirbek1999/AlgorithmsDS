"""
Time: O(n)
Space: O(n)
"""
def getTheGroups(n, query, student1, student2):
    parent = [-1 for i in range(n)]

    def find(node):
        while parent[node] >= 0:
            node = parent[node]
        return node

    for q, s1, s2 in zip(query, student1, student2):
        if q == "Friend":
            x, y = s1-1, s2-1
            x = find(x)
            if x != s1-1:
                parent[s1-1] = x
            y = find(y)
            if y != s2-1:
                parent[s2-1] = y
            if x < y: # x has more children
                parent[x] += parent[y]
                parent[y] = x
            else:
                parent[y] += parent[x]
                parent[x] = y
        else:
            return - parent[find(s1-1)] - parent[find(s2-1)]
