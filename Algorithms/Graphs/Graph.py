class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self,vertex,egde):
        self.gdict[vertex].append(egde)
    
     
    def bfs(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deqVertex = queue.pop(0)
            print(deqVertex)
            for adjacentVertex in self.gdict[deqVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
    

     # BFS - Queue
    # A----------B  # a-- b-- c-- d-- d-- e-- f--
    # |          |  1. a
    # |          |  2. b 
    # C----------D  3. c
    # |          |  4. d
    # |          |  5. e    
    # E----------F  6. f  
                    

    def dfs(self,vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

    # DFS -- Stack
    # A----------B  # d --5
    # |          |  # f --4
    # |          |  # d -- Already visited
    # C----------D  # e -- 3
    # |          |  # c --2
    # |          |  # b  -- 6
     # E----------F  # a -- 1
    
