class Graph():
    def __init__(self):
        self.graph = {}
    
    def add_node(self,v):
        if v in self.graph:
            print("v already exist")
        else:
            self.graph[v] = []
    
    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            print("node not exist")
        elif v2 not in self.graph:
            print("node not exist")
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
    
    def delete_node(self,v):
        if v not in self.graph:
            print("node not exxist")
        else:
            self.graph.pop(v)
            for i in self.graph:
                list1 = self.graph[i]
                if v in list1:
                    list1.remove(v)

    def dfs(self,start,visited = None):
        if visited is None:
            visited = set()
        if start not in visited:
            print(start,end=" ")
            visited.add(start)
            for neighbor in self.graph[start]:
                self.dfs(neighbor,visited)

    def bfs(self,start):
        visited = set()
        queue = []
        queue.append(start)
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node,end=" ")
                visited.add(node)
                queue.extend(self.graph[node])
                
    def display(self):
        print(self.graph)
    
graph = Graph()
graph.add_node(10)
graph.add_node(20)
graph.add_node(30)
graph.add_edge(10,20)
graph.delete_node(30)
graph.display()
graph.dfs(10)