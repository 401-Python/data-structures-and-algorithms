from linked_list import Node, LinkedList

def test_list_creation():
  actual = LinkedList()
  assert actual.head == None

def test_insert_method():
  lst_one = LinkedList()
  lst_one.insert(1)
  lst_one.insert(2)
  lst_one.insert(3)

  assert lst_one.head.val == 3
  assert lst_one.head.next.val == 2
  assert lst_one.head.next.next.val == 1

def test_includes_method():
  lst_two = LinkedList()
  lst_two.insert('apples')
  lst_two.insert('pickles')
  lst_two.insert('chips')

  assert lst_two.includes('pickles') == True
  assert lst_two.includes('whales') == False

def test_to_string_method():
  lst_three = LinkedList()
  lst_three.insert(3)
  lst_three.insert(4)
  lst_three.insert(5)

  actual = lst_three.to_string()
  expected = [5, 4, 3]
  assert actual == expected
  



