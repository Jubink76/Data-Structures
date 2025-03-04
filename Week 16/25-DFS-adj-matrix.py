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

    def dfs(self,node):
        if node not in self.nodes:
            print("given node is not present")
            return
        visited = set()
        stack = []
        stack.append(node)
        while stack:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.add(current)
                index = self.nodes.index(current)
                for i in range(self.node_count):
                    if self.graph[index][i] == 1 and self.nodes[i] not in visited:
                        stack.append(self.nodes[i])

        # to check the graph is conncected or disconnected
        for i in self.nodes:
            if i not in visited:
                print("Given graph is a disconnected graph")
                break
        else:
            print("Grah is a connected graph")

    def traverse_all(self):
        visited = set()
        count = 0

        for i in self.ndoes:
            if i not in visited:
                count += 1
                self.dfs(i,visited)  

        if count > 1:
            print("disconnected graph")
        else:
            print("connected graph")  

    def display_graph(self):
        for i in range(self.node_count):
            for j in range(self.node_count):
                print(self.graph[i][j], end=" ")
            print()

graph = Graph()
graph.add_node("a")
graph.add_node("b")
graph.add_node("c")
graph.add_node("d")
print(graph.nodes)
print(graph.graph)
graph.add_edge("a","b")
graph.add_edge("a","c")
graph.dfs("b")
graph.display_graph()
            