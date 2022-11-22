"""
Time: O(V * E)
Space: O(V * E)
"""


def detectCycleUtil(graph, visited, inRecStack, source):

    visited[source] = True
    inRecStack[source] = True

    for neighbor in graph[source]:
        if not visited[neighbor]:
            if detectCycleUtil(graph, visited, inRecStack, neighbor):
                return True
        elif inRecStack[neighbor]:
            return True
    
    inRecStack[source] = False
    visited[source] = False

    return False


def detectCycle(graph):

    visited = {vertex:False for vertex in graph}
    inRecStack = {vertex:False for vertex in graph}

    
    for vertex in graph.keys():
        if not visited[vertex]:
            if detectCycleUtil(graph, visited, inRecStack, vertex):
                return True

    return False
