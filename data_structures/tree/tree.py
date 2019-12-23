class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def in_order(self, node=None, results=[]):
      node = node or self.root

      if node.left:
        self.in_order(node.left, results)
      
      results.append(node.value)

      if node.right:
        self.in_order(node.right, results)

      return results


    def pre_order(self, node=None, results=[]):
      node = node or self.root

      results.append(node.value)

      if node.left:
        self.pre_order(node.left, results)

      if node.right:
        self.pre_order(node.right, results)

      return results

    def post_order(self, node=None, results=[]):

      node = node or self.root

      if node.left:
        self.post_order(node.left, results)

      if node.right:
        self.post_order(node.right, results)
      
      results.append(node.value)

      return results


class BinarySearchTree(BinaryTree):

  def add(self, value):
    node = Node(value)
    if not self.root:
      self.root = node
      return
    
    if value < self.root.value:
      if not self.root.left:
        self.root.left = node
    else:
      if not self.root.right:
        self.root.right = node
        
  def contains(self, value, current=None):
      current = current or self.root
      if not self.root or value == None:
        return False
    
      if current.value == value:
        print('yes')
        return True
      elif current.value > value:
        return self.contains(value, current.left)
      else:
        return self.contains(value, current.right)

tree = BinarySearchTree()
tree.add(20)
tree.add(15)
tree.add(10)

# print(tree.post_order())
print(tree.in_order())
print(tree.pre_order())
