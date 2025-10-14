# from https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
# do a dfs or bfs for a residual graph

from collections import defaultdict
#import graphlib

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
        #print(self.ROW)

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0
        
        while self.bfs(source, sink, parent):
            flow = float("Inf")
            s = sink
            while(s != source):
                flow = min(flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= flow
                self.graph[v][u] += flow
                v = parent[v]
        return max_flow

    def bfs(self, s, t, parent):
        # indicate which node has been visited
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for index, val in enumerate(self.graph[u]):
                if visited[index] == False and val > 0:
                    queue.append(index)
                    visited[index] = True
                    parent[index] = u
                    if index == t:
                        return True
        return False


# adjacency matrix for a graph from 
# https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
graph = [
	[ 0, 16,  13, 0,  0,  0 ],
    [ 0,  0, 10, 12,  0,  0 ],
    [ 0,  4,  0,  0, 14,  0 ],
    [ 0,  0,  9,  0,  0, 20 ],
    [ 0,  0,  0,  7,  0,  4 ],
    [ 0,  0,  0,  0,  0,  0 ]
]
# hw4 figure 1
# s: 0, u: 1, v:2, w:3, x:4, t:5
graph1 = [[0, 8, 0, 0, 0, 0],
[0, 0, 0, 3, 0, 5],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 3],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0]]
source = 0
sink = 5
flow = Graph(graph)
flow1 = Graph(graph1)
print(flow.ford_fulkerson(source, sink))
print(flow.ford_fulkerson(source, sink))