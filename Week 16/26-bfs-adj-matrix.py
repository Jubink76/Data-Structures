class Graph():
    def __init__(self):
        self.nodes = []
        self.graph = []
        self.node_count = 0

    def add_node(self,v):
        if v in self.nodes:
            print("Node is present")
        else:
            self.node_count += 1
            self.nodes.append(v)
            for i in self.graph:
                i.append(0)
            temp = []
            for i in range(self.node_count):
                temp.append(0)
            self.graph.append(temp)
    # if the weighted add one more parametere(v1,v2,cost)
    def add_edge(self,v1,v2):
        if v1 not in self.nodes:
            print("given node is not present")
        elif v2 not in self.nodes:
            print("given nodde is not present")
        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)
            # if weighted instead of 1 assign cost
            self.graph[index1][index2] = 1
            self.graph[index2][index1] = 1

    def bfs(self,node):
        if node not in self.nodes:
            print("Node not present")
            return
        visited = set()
        queue = []
        queue.append(node)
        while queue:
            current = queue.pop()# Dequeue
            if current not in visited:
                print(current)
                visited.add(current)
                index = self.nodes.index(current)
                for i in range(self.node_count):
                    if self.graph[index][i] == 1 and self.nodes[i] not in visited:
                        queue.append(self.nodes[i]) # Enqueue adjacent node


graph = Graph()
graph.add_node("a")
graph.add_node("b")
graph.add_node("c")
graph.add_node("d")
print(graph.nodes)
print(graph.graph)
graph.add_edge("a","b")
graph.add_edge("a","c")
graph.bfs("b")
