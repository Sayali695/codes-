visited = []
stack = []
def dfs_traversal(graph, node):
    visited.append(node)
    stack.append(node)

    while stack:
        m = stack.pop(-1)
        print(m, end = " ")
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                stack.append(i)

# graph = {'1': ['3', '2'], 
#          '2': ['4', '5'], 
#          '3': ['4'], 
#          '4': ['6', '8'], 
#          '5' : ['6'], 
#          '6': ['7'], 
#          '7': ['8'], 
#          '8' : []}

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
  }
dfs_traversal(graph,'5')