from fizz_buzz_tree import BinaryTree, fizz_buzz_tree, Node

def test_two_values_no_fizz():
  tree = BinaryTree()
  tree.root = Node(4)
  tree.root.left = Node(23)

  assert fizz_buzz_tree(tree).root.value == '4'
  assert fizz_buzz_tree(tree).root.left.value == '23'

def test_three_values_no_fizz():
  tree = BinaryTree()
  tree.root = Node(4)
  tree.root.left = Node(23)
  tree.root.right = Node(19)

  assert fizz_buzz_tree(tree).root.value == '4'
  assert fizz_buzz_tree(tree).root.left.value == '23'
  assert fizz_buzz_tree(tree).root.right.value == '19'

def test_fizz_buzz():
  tree = BinaryTree()
  tree.root = Node(17)
  tree.root.left = Node(15)
  tree.root.right = Node(5)
  tree.root.right.left = Node(9)

  assert fizz_buzz_tree(tree).root.value == '17'
  assert fizz_buzz_tree(tree).root.left.value == 'FizzBuzz'
  assert fizz_buzz_tree(tree).root.right.value == 'Buzz'
  assert fizz_buzz_tree(tree).root.right.left.value == 'Fizz'
  