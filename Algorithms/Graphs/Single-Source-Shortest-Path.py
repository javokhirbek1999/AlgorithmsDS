class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            self.gdict = {}
        self.gdict = gdict
    
    def bfs(self,start,end):
        queue = [start]
        while queue:
            path = queue.pop(0)
            node= path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node,[]):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
# Note: BFS works only for UNWEIGHTED Graphs
#--------------------------------------------
# How is it working:
#--------------------------------------------
# Starting point: a and Starting queue: [['a']]
# Queue: [['a']]
# Loop 1:
#  Path: ['a']
# Node: a
# Queue After popping: []
# New Path: ['a']
# Adjacent: b (Before Appending) in inner loop of 1
# New Path: ['a', 'b'] (After appending) in inner loop of 2
# New Path: ['a']
# Adjacent: c (Before Appending) in inner loop of 2
# New Path: ['a', 'c'] (After appending) in inner loop of 3




# Queue: [['a', 'b'], ['a', 'c']]
# Loop 2:
#  Path: ['a', 'b']
# Node: b
# Queue After popping: [['a', 'c']]
# New Path: ['a', 'b']
# Adjacent: d (Before Appending) in inner loop of 1
# New Path: ['a', 'b', 'd'] (After appending) in inner loop of 2
# New Path: ['a', 'b']
# Adjacent: g (Before Appending) in inner loop of 2
# New Path: ['a', 'b', 'g'] (After appending) in inner loop of 3




# Queue: [['a', 'c'], ['a', 'b', 'd'], ['a', 'b', 'g']]
# Loop 3:
#  Path: ['a', 'c']
# Node: c
# Queue After popping: [['a', 'b', 'd'], ['a', 'b', 'g']]




# Queue: [['a', 'b', 'd'], ['a', 'b', 'g']]
# Loop 4:
#  Path: ['a', 'b', 'd']
# Node: d
# Queue After popping: [['a', 'b', 'g']]
# New Path: ['a', 'b', 'd']
# Adjacent: f (Before Appending) in inner loop of 1
# New Path: ['a', 'b', 'd', 'f'] (After appending) in inner loop of 2




# Queue: [['a', 'b', 'g'], ['a', 'b', 'd', 'f']]
# Loop 5:
#  Path: ['a', 'b', 'g']
# Node: g
# Queue After popping: [['a', 'b', 'd', 'f']]
# New Path: ['a', 'b', 'g']
# Adjacent: f (Before Appending) in inner loop of 1
# New Path: ['a', 'b', 'g', 'f'] (After appending) in inner loop of 2




# Queue: [['a', 'b', 'd', 'f'], ['a', 'b', 'g', 'f']]
# Loop 6:
#  Path: ['a', 'b', 'd', 'f']
# Node: f
# Queue After popping: [['a', 'b', 'g', 'f']]
