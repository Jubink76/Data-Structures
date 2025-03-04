# graph add node and representation by using adjacency list

class Graph():
    def __init__(self):
        self.graph = {}
    
    def add_node(self,v):
        if v in self.graph:
            print("Node already exist")
        else:
            self.graph[v] = []

graph = Graph()
graph.add_node("a")
graph.add_node("b")
graph.add_node("b")
print(graph.graph)