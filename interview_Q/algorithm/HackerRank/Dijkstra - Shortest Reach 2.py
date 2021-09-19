
# Q: https://www.hackerrank.com/challenges/dijkstrashortreach/problem
import sys
from Queue import PriorityQueue


class Vertex:
    def __init__(self):
        self.edges = {}

    def get_edges(self):
        return self.edges

    def add_edge(self, value, distance):
        if value not in self.edges or distance < self.edges[value]:
            self.edges[value] = distance


class Graph:
    def __init__(self, N):
        self.vertices = {}
        while (N > 0):
            self.vertices[N] = Vertex()
            N -= 1

    def get_vertices(self):
        return self.vertices

    def get_vertex(self, value):
        return self.vertices[value]

    def add_vertex(self, value, vertex):
        self.vertices[value] = vertex


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def calculate(self, start):
        solved = {start: 0}
        adjacents = PriorityQueue()
        self.update_adjacents(start, solved, adjacents)
        while not adjacents.empty():
            (distance, value) = adjacents.get()
            if value in solved:
                continue
            solved[value] = distance
            self.update_adjacents(value, solved, adjacents)
        return solved

    def update_adjacents(self, parent, solved, adjacents):
        edges = self.graph.get_vertex(parent).get_edges()
        for value, distance in edges.items():
            adjacents.put((solved[parent] + distance, value))

# The algorithm uses a min-priority queue and runs in time O(|n|^2)(where |n| is the number of nodes).
# Fredman & Tarjan 1984 propose using a Fibonacci heap min-priority queue to optimize the running time complexity to O(|E|+|V|\log |V|)(where |E| is the number of edges). This is asymptotically the fastest known single-source shortest-path algorithm for arbitrary directed graphs with unbounded non-negative weights.
def shortestReach(n, edges, s):
    graph = Graph(n)
    for edge in edges:
        graph.get_vertex(edge[0]).add_edge(edge[1], edge[2])
        graph.get_vertex(edge[1]).add_edge(edge[0], edge[2])

    dijkstra = Dijkstra(graph)
    solvedDict = dijkstra.calculate(s)

    resultList = [-1] * n
    for key in solvedDict:
        resultList[key-1] = solvedDict[key]

    resultList.pop(s-1)

    return resultList


            
edges = [[1,2,1],[2,3,2],[1,3,4]]
print shortestReach(3, edges, 1)
# 1 2 24
# 1 4 20
# 3 1 3
# 4 3 12
# 1
edges = [[1,2,24],[1,4,20],[3,1,3],[4,3,12]]
print shortestReach(4, edges, 1)

# 5 3
# 1 2 10
# 1 3 6
# 2 4 8
# 2
edges = [[1,2,10],[1,3,6],[2,4,8]]
print shortestReach(5, edges, 2)


# -----------------

# def read_integers():
#     return [int(x) for x in sys.stdin.readline().split(" ")]


# def build_graph(N, M):
#     graph = Graph(N)
#     while (M > 0):
#         (x, y, R) = read_integers()
#         graph.get_vertex(x).add_edge(y, R)
#         graph.get_vertex(y).add_edge(x, R)
#         M -= 1
#     return graph


# def print_distances(distances, N, S):
#     for i in range(1, N + 1):
#         if (i == S):
#             continue
#         distance = -1 if i not in distances else distances[i]
#         print(distance, end=" ")
#     print()


# def execute_test_case():
#     (N, M) = read_integers()
#     graph = build_graph(N, M)
#     dijkstra = Dijkstra(graph)
#     S = int(sys.stdin.readline())
#     distances = dijkstra.calculate(S)
#     print_distances(distances, N, S)


# def main():
#     T = int(sys.stdin.readline())
#     while (T > 0):
#         execute_test_case()
#         T -= 1

# if __name__ == "__main__":
#     main()