visited = []
queue = []
def bfs_traversal(graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end = " ")
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

graph = {'1': ['3', '2'], 
         '2': ['4', '5'], 
         '3': ['4'], 
         '4': ['6', '8'], 
         '5' : ['6'], 
         '6': ['7'], 
         '7': ['8'], 
         '8' : []}
bfs_traversal(graph,'1')