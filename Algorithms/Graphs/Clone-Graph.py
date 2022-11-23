"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Recursive DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        
        clone, visited = dict(), dict()
        
        self.dfs(clone, visited, node)
        
        return clone[node]
    
    def dfs(self, clone, visited, node):
        
        if node in visited:
            return
        
        visited[node] = True
        
        if node not in clone:
            clone[node] = Node(node.val)
        
        for neigh in node.neighbors:
            if neigh not in clone:
                clone[neigh] = Node(neigh.val)
            clone[node].neighbors.append(clone[neigh])
            self.dfs(clone, visited, neigh)
        


# Iterative DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        
        clone, visited, stack = dict(), dict(), collections.deque([node])
        
        while stack:
            
            curr = stack.pop()
            
            if curr in visited:
                continue
            
            if curr not in clone:
                clone[curr] = Node(curr.val)
            
            visited[curr] = True
            
            for neighbor in curr.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                clone[curr].neighbors.append(clone[neighbor])
                stack.append(neighbor)
        
        return clone[node]



# BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        
        clone, visited, queue = dict(), dict(), collections.deque([node])
        
        while queue:
            
            curr = queue.popleft()
            
            if curr in visited:
                continue
            
            visited[curr] = True
            
            if curr not in clone:
                clone[curr] = Node(curr.val)
            
            for neighbor in curr.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                clone[curr].neighbors.append(clone[neighbor])
                queue.append(neighbor)
        
        return clone[node]
