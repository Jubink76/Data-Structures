# graph add node and representation by using adjacency list

class Graph():
    def __init__(self):
        self.graph = {}
    
    def add_node(self,v):
        if v in self.graph:
            print("Node already exist")
        else:
            self.graph[v] = []
    
    def delete_node(self,v):
        if v not in self.graph:
            print("node is not present")
        else:
            self.graph.pop(v)
            for i in self.graph:
                list1 = self.graph[i]
                if v in list1:
                    list1.remove(v)
                # for weighted graph
                # for j in list1:
                    # if v == j[0]:
                        # list1.remove[j]
                            # break



graph = Graph()
graph.add_node("a")
graph.add_node("b")
graph.add_node("c")
graph.delete_node("c")
print(graph.graph)