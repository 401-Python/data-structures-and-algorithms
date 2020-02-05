def depth_first(graph, start, visited=None):
    '''
    This function takes in a graph as an adjacency list
    and performs a dfs, printing each vertex
    '''
    if visited is None:
        visited = set() # create a set to add each visited vertex/node
    print(start)
    visited.add(start) # add the first vertex and print it

    for next in graph[start] - visited: # recurse until every node is visited
        depth_first(graph, next, visited) 
    return visited

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}
depth_first(graph, '0')