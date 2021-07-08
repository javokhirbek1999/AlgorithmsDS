import sys

class Graph:
	def __init__(self, vertexNum, edges, nodes):
		self.edges = edges
		self.nodes = nodes
		self.vertexNum = vertexNum
		self.MST = []

	def printSolution(self):
		print('Edge: Weight')
		for s,d,w in self.MST:
			print("%s -> %s: %s" % (s, d, w))

	def prims(self):
		visited = [0]*self.vertexNum
		edgeNum = 0
		visited[0]=True
		while edgeNum<self.vertexNum-1:
			min_weight = sys.maxsize # <- infinity
			for i in range(self.vertexNum):
				if visited[i]:
					for j in range(self.vertexNum):
						if ((not visited[j]) and self.edges[i][j]):
							if min_weight > self.edges[i][j]:
								min_weight = self.edges[i][j]
								s = i
								d = j
			self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
			visited[d] = True
			edgeNum += 1
		self.printSolution()
