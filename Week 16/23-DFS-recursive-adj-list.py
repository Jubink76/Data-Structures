# DFS using Recursive aproach using adjacency list representation

class Graph():
    def __init__(self):
        self.graph = {}
    
    def add_node(self,v):
        if v in self.graph:
            print("Node already exist")
        else:
            self.graph[v] = []
    
    def add_edge(self,v1,v2):
        if v1 not in self.graph:
            print("given node is not present")
        elif v2 not in self.graph:
            print("given node is not preesent")
        else:
            # if the graph is undirected unweighted:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
        
    def DFS(self,node,visited=None):
        if node not in self.graph:
            print("Node not present in the graph")
            return
        if visited is None:
            visited = set()
        if node in visited:
            return
        
        print(node)
        visited.add(node)
        for i in self.graph[node]:
            self.DFS(i,visited)

        
graph = Graph()
graph.add_node("a")
graph.add_node("b")
graph.add_node("c")
graph.add_node("d")
graph.add_edge("a","b")
graph.add_edge("a", "c")
graph.DFS("a")
print(graph.graph)