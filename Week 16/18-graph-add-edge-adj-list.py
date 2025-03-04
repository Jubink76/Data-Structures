class Graph():
    def __init__(self):
        self.graph = {}
    
    def add_node(self,v):
        if v in self.graph:
            print("Node already exist")
        else:
            self.graph[v] = []
    
    # def add_edge(self,v1,v2):
    #     if v1 not in self.graph:
    #         print("given node is not present")
    #     elif v2 not in self.graph:
    #         print("given node is not preesent")
    #     else:
    #         # if the graph is undirected unweighted:
    #         self.graph[v1].append(v2)
    #         self.graph[v2].append(v1)
           
    # if the graph is weighted add cost parameter to this funciton(v1,v2,cost)
    def add_edge(self,v1,v2,cost):
        if v1 not in self.graph:
            print("given node is not present")
        elif v2 not in self.graph:
            print("given node is not preesent")
        else:
            # if weighted instead of vertices update weight
            list1 = [v2,cost]
            list2 = [v1,cost]
            self.graph[v1].append(list1)
            self.graph[v2].append(list2)

graph = Graph()
graph.add_node("a")
graph.add_node("b")
graph.add_node("b")
graph.add_edge("a","b",10)
print(graph.graph)