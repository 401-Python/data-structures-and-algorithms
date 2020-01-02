class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    

    def in_order(self, node=None, results=None):
      node = node or self.root

      results = results or []
      if node:
        if node.left:
          self.in_order(node.left, results)
        
        results.append(node.value)

        if node.right:
          self.in_order(node.right, results)

      return results


    def pre_order(self, node=None, results=None):
      node = node or self.root

      results = results or []

      if node:
        results.append(node.value)

        if node.left:
          self.pre_order(node.left, results)

        if node.right:
          self.pre_order(node.right, results)

      return results

    def post_order(self, node=None, results=None):

      node = node or self.root

      results = results or []
      if node:
        if node.left:
          self.post_order(node.left, results)

        if node.right:
          self.post_order(node.right, results)
        
        results.append(node.value)

      return results
    
    def find_max_val(self, root):
      if not root:
        return None
      
      max_val = root.value
      left_val = self.find_max_val(root.left)
      right_val = self.find_max_val(root.right)

      if root.left:
        if left_val > max_val:
          max_val = left_val
      if root.right:
        if right_val > max_val:
          max_val = right_val
      
      return max_val


class BinarySearchTree(BinaryTree):

  def add(self, value, root=None):
    root = root or self.root

    node = Node(value)

    if not self.root:
      self.root = node
      return
    
    if value < root.value:
      if root.left:
        self.add(value, root.left)
      else:
        root.left = node
    else:
      if root.right:
        self.add(value, root.left)
      else:
       root.right = node
    

  def contains(self, value, current=None):
      current = current or self.root

      if not self.root or value == None:
        print('no')
        return False
    
      if current.value == value:
        print('yes')
        return True
      elif current.value < value:
        return self.contains(value, current.left)
      else:
        return self.contains(value, current.right)
      
      print('no')
      return False

  


if __name__ == "__main__":
  tree = BinarySearchTree()
  tree.root = Node(5)
  tree.root.left = Node(19)
  tree.root.right = Node(7)
  tree.root.left.left = Node(23)
  tree.root.left.right = Node(8)

  print(tree.find_max_val(tree.root))

