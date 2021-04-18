visited =set()

def dfs(graph,node):

    if node not in visited:
        print(node)
        visited.add(node)

        for vertex in graph[node]:
            dfs(graph,vertex)
        

####Driver code####
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
dfs(graph,'A')

"""
Time Complexity
Since all the nodes and vertices are visited, the average time complexity for DFS on a graph is O(V + E), where V is the number of vertices and E is the number of edges.
In case of DFS on a tree, the time complexity is O(V), where VV is the number of nodes.

We say average time complexity because a set’s in operation has an average time complexity of O(1). 
If we used a list, the complexity would be higher.
"""