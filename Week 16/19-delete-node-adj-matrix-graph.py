
class Graph():
    def __init__(self):
        self.node = []
        self.graph = []
        self.node_count = 0

    def add_node(self,v):
        if v in self.node:
            print("Node is present")
        else:

            self.node_count += 1
            self.node.append(v)
            for i in self.graph:
                i.append(0)
            temp = []
            for i in range(self.node_count):
                temp.append(0)
            self.graph.append(temp)
    def delete_node(self,v):
        if v not in self.node:
            print("Node not present")
        else:
            index = self.node.index(v)
            self.node_count -= 1
            self.node.remove(v)
            self.graph.pop(index)
            for i in self.graph:
                i.pop(index)

    # Display function to display the matrix format of the currenet nodes
    def display_graph(self):
        for i in range(self.node_count):
            for j in range(self.node_count):
                print(self.graph[i][j],end=" ")
            print()


graph = Graph()
graph.add_node(10)
graph.add_node(20)
graph.add_node(30)
graph.delete_node(30)
print(graph.node)
print(graph.graph)
graph.display_graph()