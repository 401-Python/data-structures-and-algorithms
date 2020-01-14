from insertion_sort import insertion_sort

def test_regular_case():
  ints = [9, 5, 4, 3, 7, 1]
  assert insertion_sort(ints) == [1,3,4,5,7,9]

def test_duplicate_minimum():
  ints = [2, 1, 1, 5, 4]
  assert insertion_sort(ints) == [1,1,2,4,5]

def test_with_negatives():
  ints = [1, 0, -1, 4, 3]
  assert insertion_sort(ints) == [-1,0,1,3,4]