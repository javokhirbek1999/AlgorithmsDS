INFINITY = 9999
def printSolution(numVertices, distance):
    for i in range(numVertices):
        for j in range(numVertices):
            if(distance[i][j] == INFINITY):
                print('INFINITY', end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")

def floydWarshall(numVertices, graph):
    distance = graph
    for k in range(numVertices):
        for i in range(numVertices):
            for j in range(numVertices):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    
    printSolution(numVertices, distance)
