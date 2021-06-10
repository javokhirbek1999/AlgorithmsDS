class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []
    
    def add_edge(self,s,d,w):
        self.graph.append([s,d,w])
    
    def addNode(self,value):
        self.nodes.append(value)
    
    def print_solution(self,dist):
        print("Vertex Distance from Source: ")
        for key, value in dist.items():
            print(' ' + key, ' :  ',value)

    def bellmanFord(self,source):
        distances = {i:float("Infinity") for i in self.nodes}
        distances[source] = 0

        for _ in range(self.v-1):
            for s, d, w in self.graph:
                 if distances[s] != float("Infinity") and distances[s] + w < distances[d]:
                    distances[d] = distances[s]+w
        
        for s,d,w in self.graph:
            if distances[s] != float("Infinity") and distances[s] + w < distances[d]:
                print("Graph contains negative cycle")
                return 
        
        self.print_solution(distances)
