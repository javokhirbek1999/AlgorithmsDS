from collections import defaultdict

class Graph:
    def __init__(self,numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices
    
    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)
    
    def toplogicalSortUtil(self,vertex,visited,stack):
        visited.append(vertex)

        for i in self.graph[vertex]:
            if i not in visited:
                self.toplogicalSortUtil(i,visited,stack)
        
        stack.insert(0,vertex)
    
    def toplogicalSort(self):

        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.toplogicalSortUtil(k,visited,stack)
        
        print(stack) 
