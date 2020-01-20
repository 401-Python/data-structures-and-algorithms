from hash_table import HashTable, LinkedList

def test_add_key():
  ht = HashTable()
  ht.add('keyTest', 1)
  assert ht.contains('keyTest') == True

def test_add_multiple():
  ht = HashTable()
  ht.add('one', 1)
  ht.add('two', 2)
  ht.add('three', 3)
  assert ht.contains('one') == True
  assert ht.contains('two') == True
  assert ht.contains('three') == True

def test_contains():
  ht = HashTable()
  ht.add('four', 4)
  assert ht.contains('four') == True
  assert ht.contains('whale') == False

def test_get():
  ht = HashTable()
  ht.add('five', 5)
  assert ht.get('five') == 5
  assert ht.get('tiger') == None

