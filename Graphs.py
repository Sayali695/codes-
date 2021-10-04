class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph = {}
        for start,end in self.edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]
        print(self.graph)

    
routes = [
    ("Mumbai","Pune"),
    ("Nashik", "Ahmednagar"),
    ("Ahmednagar", "Pune"),
    ("Pune","Ratnagiri"),
    ("Mumbai","Ratnagiri"),
    ("Pune", "Nagpur")
]
r1 = Graph(routes)