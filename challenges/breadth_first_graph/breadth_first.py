import collections

def breadth_first(graph, root): 
  '''
  This function takes in a grapth and a root vertices
  First we add the root to the back of queue
  Then we take from the front of the queue and add it to visited
  Then create a list of this vertex's adjacent nodes and add unvisited to back of queue
  Repeat until queue is empty
  '''
  visited = set()
  queue = collections.deque([root])
  visited.add(root)
  while queue: 
      vertex = queue.popleft() # programiz.com - couldn't find name of author on page
      for neighbour in graph[vertex]: 
          if neighbour not in visited: 
              visited.add(neighbour) 
              print(neighbour)
              queue.append(neighbour) 

def bfs(graph, start_node, end_node):
  visited = set()
  queue = collections.deque([start_node])
  visited.add(start_node)

  while queue:
    vertex = queue.popleft()
    for neighbor in graph[vertex]:
      if neighbor == end_node:
        return True
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
  
  return False
      

if __name__ == "__main__":
 graph = { 
 0: [1, 2], 
 1: [2], 
 2: [3], 
 3: [1,2] 
 } 
 bfs(graph, 0, 2)



