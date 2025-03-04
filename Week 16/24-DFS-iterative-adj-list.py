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
    
    def dfs_iter(self,node):
        visited = set()
        if node not in self.graph:
            print("Given node is not present")
            return
        stack = []
        stack.append(node)
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.add(current)
                for i in self.graph[current]:
                    stack.append(i)
    

graph = Graph()
graph.add_node("a")
graph.add_node("b")
graph.add_node("c")
graph.add_edge("a","b")
graph.add_edge("a", "c")
graph.dfs_iter("a")
print(graph.graph)