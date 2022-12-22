'''
V = # of vertices
E = # of edges

Time: O(V+E)
Space: O(V+E)
'''

from collections import defaultdict, deque


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:


        graph = defaultdict(list)

        for v1,v2 in dislikes:
            graph[v1].append(v2)
            graph[v2].append(v1)
        

        colors = [-1] * (n+1)


        for node in range(1, n+1):
            if colors[node] == -1:
                if not self.bipartite(node, graph, colors):
                    return False
        
        return True
    
    
    def bipartite(self, node: int, graph: DefaultDict[int, List[int]], colors: List[int]) -> bool:

        queue = deque()

        queue.append(node)
        
        colors[node] = 1

        while queue:

            current = queue.popleft()

            for neighbor in graph[current]:
                if colors[neighbor] == colors[current]:
                    return False
                
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[current]
                    queue.append(neighbor)
        
        return True

