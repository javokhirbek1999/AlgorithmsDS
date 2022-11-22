"""
Time: O(V * E)
Space: O(V * E)
"""
def detectCycleUD_Util(graph, vertex, vertexStatus):
    if not vertex in graph:
        return False

    if vertexStatus[vertex] == 2:
        return True

    vertexStatus[vertex] = 1
    
    for neighbor in graph[vertex]:
        
        if neighbor not in vertexStatus: continue

        if vertexStatus[neighbor] == 1:
            vertexStatus[neighbor] = 2
        
        elif detectCycleUD_Util(graph, neighbor, vertexStatus):
            return True
    
    return False


def detectCycleUD(graph):

    vertexStatus = {vertex:0 for vertex in graph}

    for vertex in graph:

        vertexStatus[vertex] = 1

        for neighbor in graph[vertex]:
            if detectCycleUD_Util(graph, neighbor, vertexStatus):
                return True

        vertexStatus[vertex] = 0
    
    return False
