from collections import deque

class _Node:
    """Protected Tree Node"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Queue:
    """Implementation of Queue that "composes" built in deque class"""

    def __init__(self):
        self._dq = deque()

    def enqueue(self, value):
        self._dq.appendleft(value)

    def dequeue(self):
        return self._dq.pop()

    def peek(self):
        return self._dq[-1]

    def is_empty(self):
        return len(self._dq) == 0


class BinaryTree:
    """Simple BinaryTree with enough functionality for breadth first adding"""

    def __init__(self):
        self._root = None
    

    def add(self, value):

        node = _Node(value)

        if not self._root:
            self._root = node
            return

        q = Queue()

        q.enqueue(self._root)

        while not q.is_empty():

            current = q.dequeue()

            if current.left:
                q.enqueue(current.left)
            else:
                current.left = node
                break

            if current.right:
                q.enqueue(current.right)
            else:
                current.right = node
                break

def breadth_first(root): 
    levels = []
    if not root:
      return levels
      
    def helper(node, level):
        # start the current level and append an empty list
        # the level starts at 0 and we add 1 during each pass
        # after appending the current node value
        
        if len(levels) == level:
            levels.append([])

        # append the current node value
        levels[level].append(node.value)

        # process child nodes for the next level
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)
          
    helper(root, 0)
    print(levels)
    return levels

if __name__ == "__main__":  
  tree = BinaryTree()
  tree.add(5)
  tree.add(4)
  tree.add(3)
  tree.add(2)
  tree.add(1)

  breadth_first(tree._root)


  print(tree._root.value)