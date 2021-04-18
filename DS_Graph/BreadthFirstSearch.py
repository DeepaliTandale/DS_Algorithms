visited = []
queue = []

def bfs(graph,node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print(s,end=' ')

    for vertex in graph[s]:
      if vertex not in visited:
        visited.append(vertex)
        queue.append(vertex)

    #print(visited)
####Driver code####
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
bfs(graph,'A')

"""
The time complexity of BFS if the entire tree is traversed is O(V) where V is the number of nodes. 
In the case of a graph, the time complexity is O(V + E) where V is the number of vertexes and E is the number of edges.
"""